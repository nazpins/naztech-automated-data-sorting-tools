from transformers import pipeline
import re

def preprocess_text(text: str) -> str:
    return text.lower()

def extract_command(text: str):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    commands = ['organize files', 'remove duplicates', 'disk cleanup', 'registry cleanup', 'optimize startup', 'defragment disk']
    result = classifier(text, candidate_labels=commands, multi_label=False)
    return result['labels'][0], result['scores'][0]

def extract_path(text: str):
    pattern = r"[C-Z]:\\[^\\:*?\"<>|\r\n]+\\[^\\:*?\"<>|\r\n]*"
    match = re.search(pattern, text)
    return match.group(0) if match else "No path detected"

def process_user_input(user_input: str):
    text = preprocess_text(user_input)
    command, confidence = extract_command(text)
    path = extract_path(text)
    return command, path
