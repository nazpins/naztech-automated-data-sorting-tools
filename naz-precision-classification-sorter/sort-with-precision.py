import os
import shutil
import logging
import concurrent.futures
from transformers import pipeline
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

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
        'Advertisement', 'Miscellaneous Text'
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
        # Add file extensions and their corresponding folders here
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

    folder_path = os.path.join(directory, folder_name)
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

if __name__ == '__main__':
    print("\033[1;34mSORT WITH PRECISION - Powered by AI\033[0m")
    directory = input("Enter the directory path: ")
    organize_files_by_type(directory)
