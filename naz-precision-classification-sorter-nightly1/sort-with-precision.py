import os
import shutil
import logging
import concurrent.futures
from transformers import pipeline
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import transformers

# Suppress model conversion warnings
transformers.logging.set_verbosity_error()
logging.getLogger("transformers.modeling_tf_utils").setLevel(logging.ERROR)

# Ensure TensorFlow uses GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print("Exception during GPU setup: ", e)

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses most TensorFlow logs, except critical ones
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)  # Suppress deprecated function warnings

# Initialize classifiers
text_classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
image_model = ResNet50(weights='imagenet')

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def classify_text(text):
    categories = [
        'Article', 'Research Paper', 'Report', 'Newsletter', 'Manual',
        'Legal Document', 'Presentation', 'Creative Writing', 'Email', 'Forum Post',
        'Social Media Content', 'Technical Documentation', 'News Article', 'Blog Post',
        'Advertisement', 'Miscellaneous Text', 'Correspondence', 'Financial Document',
        'Proposal', 'Contract', 'Meeting Minutes', 'Memo', 'Brochure', 'Case Study',
        'Press Release', 'Speech Transcript', 'Review', 'Interview Transcript',
        'Whitepaper', 'Thesis', 'Essay', 'Journal Entry', 'Outline', 'Screenplay',
        'Poem', 'Short Story', 'Novel Excerpt', 'Code Documentation', 'User Guide',
        'FAQ', 'Product Description', 'Grant Proposal', 'Business Plan',
        'Technical Report', 'Scientific Article', 'Conference Paper', 'Book Chapter',
        'Magazine Article', 'Editorial', 'Opinion Piece', 'News Release', 'Feature Article',
        'Testimonial', 'Success Story', 'Biography', 'Autobiography', 'Personal Narrative',
        'Travel Writing', 'Sports Writing', 'Food Writing', 'Fashion Writing', 'Music Review',
        'Film Review', 'Book Review', 'Product Review', 'Restaurant Review', 'App Review',
        'Legal Brief', 'Court Document', 'Affidavit', 'Disclaimer', 'Terms and Conditions',
        'End-User License Agreement (EULA)', 'Non-Disclosure Agreement (NDA)', 'Memorandum of Understanding (MOU)',
        'Letter of Intent (LOI)', 'Cease and Desist Letter', 'Legal Complaint', 'Pleading',
        'Medical Record', 'Prescription', 'Medical Report', 'Patient History', 'Discharge Summary',
        'Clinical Trial Protocol', 'Informed Consent Form', 'Laboratory Report', 'Pathology Report',
        'Financial Statement', 'Balance Sheet', 'Income Statement', 'Cash Flow Statement',
        'Budget', 'Invoice', 'Receipt', 'Purchase Order', 'Expense Report',
        'Curriculum Vitae (CV)', 'Resume', 'Cover Letter', 'Recommendation Letter', 'Resignation Letter',
        'Performance Review', 'Employee Handbook', 'Training Manual', 'Standard Operating Procedure (SOP)',
        'Pitch Deck', 'Investor Presentation', 'Market Research Report', 'Competitor Analysis',
        'SWOT Analysis', 'Marketing Plan', 'Social Media Strategy', 'Content Calendar',
        'Press Kit', 'Media Advisory', 'Fact Sheet', 'Backgrounder', 'Company Profile',
        'Nonprofit Annual Report', 'Donor Appeal', 'Volunteer Handbook', 'Grant Report',
        'Academic Essay', 'Research Proposal', 'Literature Review', 'Dissertation', 'Annotated Bibliography',
        'Conference Abstract', 'Lecture Notes', 'Course Syllabus', 'Lesson Plan', 'Educational Handout',
        'Recipe', 'Crafting Instructions', 'DIY Guide', 'Troubleshooting Guide', 'Installation Guide',
        'API Documentation', 'README File', 'Changelog', 'Code Comment', 'Commit Message',
        'Sermon', 'Devotional', 'Prayer', 'Liturgy', 'Hymn Lyrics',
        'Song Lyrics', 'Album Review', 'Concert Review', 'Artist Biography', 'Discography',
        'Architectural Plan', 'Interior Design Proposal', 'Landscape Design', 'Construction Bid',
        'Appraisal Report', 'Property Listing', 'Tenant Agreement', 'Lease Agreement',
        'Shareholder Agreement', 'Partnership Agreement', 'Joint Venture Agreement', 'Franchise Agreement',
        'Distribution Agreement', 'Consulting Agreement', 'Independent Contractor Agreement', 'Confidentiality Agreement',
        'Intellectual Property Agreement', 'Licensing Agreement', 'Service Level Agreement (SLA)', 'Master Service Agreement (MSA)',
        'Statement of Work (SOW)', 'Request for Proposal (RFP)', 'Request for Quote (RFQ)', 'Scope of Work',
        'Business Continuity Plan', 'Disaster Recovery Plan', 'Risk Assessment', 'Incident Report',
        'Change Management Plan', 'Project Charter', 'Project Plan', 'Project Status Report',
        'Meeting Agenda', 'Meeting Notes', 'Conference Call Minutes', 'Webinar Recording',
        'Training Video', 'Video Tutorial', 'Product Demo', 'Explainer Video',
        'Infographic', 'Data Visualization', 'Chart', 'Graph', 'Diagram',
        'Flowchart', 'Mind Map', 'Wireframe', 'Mockup', 'Prototype',
        'Technical Drawing', 'Schematic', 'Circuit Diagram', 'Block Diagram', 'UML Diagram',
        'Software Design Document', 'Software Requirements Specification', 'Test Plan', 'Test Case',
        'Bug Report', 'Release Notes', 'User Acceptance Testing (UAT) Report', 'Post-Implementation Review',
        'White Paper', 'Case Study', 'Technical Brief', 'Application Note',
        'Data Sheet', 'Product Brochure', 'Product Catalog', 'User Manual',
        'Installation Guide', 'Quick Start Guide', 'Maintenance Guide', 'Troubleshooting Guide',
        'API Reference', 'SDK Documentation', 'Developer Guide', 'Integration Guide',
        'Style Guide', 'Brand Guidelines', 'Design System', 'Pattern Library',
        'Icon Set', 'Font Family', 'Color Palette', 'Accessibility Guidelines',
        'Usability Report', 'User Persona', 'User Journey Map', 'Customer Feedback',
        'Testimonial', 'Case Study', 'Success Story', 'Press Coverage',
        'News Clip', 'Media Mention', 'Analyst Report', 'Industry Report',
        'Market Trend', 'Competitive Landscape', 'Benchmark Report', 'Survey Report',
        'Infographic Report', 'Data Report', 'Annual Report', 'Sustainability Report',
        'Corporate Social Responsibility (CSR) Report', 'Environmental Impact Statement', 'Carbon Footprint Report', 'Energy Audit Report',
        'Safety Manual', 'Material Safety Data Sheet (MSDS)', 'Injury Report', 'Accident Report',
        'Emergency Response Plan', 'Evacuation Plan', 'Fire Safety Plan', 'Hazard Communication Plan',
        'Quality Manual', 'Quality Policy', 'Quality Procedure', 'Inspection Report',
        'Audit Report', 'Corrective Action Report', 'Preventive Action Report', 'Calibration Report',
        'Validation Report', 'Verification Report'
    ]
    prediction = text_classifier(text, candidate_labels=categories, multi_label=False)
    return prediction['labels'][0]
def classify_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = image_model.predict(x)
    return decode_predictions(preds, top=1)[0][0][1]

def process_file(file_path, directory):
    filename = os.path.basename(file_path)
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    extension_folders = {
        '.txt': 'Text Files',
        '.doc': 'Word Documents',
        '.docx': 'Word Documents',
        '.pdf': 'PDF Files',
        '.md': 'Markdown Files',
        '.jpg': 'JPEG Images',
        '.jpeg': 'JPEG Images',
        '.png': 'PNG Images',
        '.gif': 'GIF Images',
        '.bmp': 'BMP Images',
        '.xlsx': 'Excel Files',
        '.csv': 'CSV Files',
        '.ppt': 'PowerPoint Presentations',
        '.pptx': 'PowerPoint Presentations',
        '.zip': 'Compressed Archives',
        '.rar': 'Compressed Archives',
        '.7z': 'Compressed Archives',
        '.tar': 'Compressed Archives',
        '.gz': 'Compressed Archives',
        '.mp3': 'Audio Files',
        '.wav': 'Audio Files',
        '.mp4': 'Video Files',
        '.avi': 'Video Files',
        '.mov': 'Video Files',
        '.mkv': 'Video Files',
        '.py': 'Python Scripts',
        '.js': 'JavaScript Files',
        '.html': 'HTML Files',
        '.css': 'CSS Files',
        '.json': 'JSON Files',
        '.xml': 'XML Files'
    }

    if extension in ['.txt', '.doc', '.docx', '.pdf', '.md']:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read(5000)
                folder_name = classify_text(content)
        except Exception as e:
            logging.error(f"Error reading {filename}: {str(e)}")
            folder_name = 'Unclassified'
    elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        folder_name = classify_image(file_path)
    else:
        folder_name = extension_folders.get(extension, 'Other')

    sorted_output_folder = os.path.join(directory, "Sorted_Output")
    folder_path = os.path.join(sorted_output_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    destination_path = os.path.join(folder_path, filename)
    try:
        shutil.move(file_path, destination_path)
        logging.info(f"Moved {filename} to {folder_name} folder.")
    except Exception as e:
        logging.error(f"Error moving {filename}: {str(e)}")

def organize_files_by_type(directory):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                futures.append(executor.submit(process_file, file_path, directory))

        concurrent.futures.wait(futures)

    # Delete empty folders
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                logging.info(f"Removed empty folder: {dir_path}")

if __name__ == '__main__':
    print("\033[1;34mSORT WITH PRECISION - Powered by AI\033[0m")
    print("Enter the directory path to organize files (e.g., C:\\path\\to\\directory):")
    directory = input()
    try:
        organize_files_by_type(directory)
        print("\033[1;32mFile organization completed successfully!\033[0m")
    except Exception as e:
        print(f"\033[1;31mAn error occurred during file organization: {str(e)}\033[0m")