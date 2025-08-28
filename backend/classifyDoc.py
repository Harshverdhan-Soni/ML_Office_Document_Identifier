import sys
import joblib
import os
from PyPDF2 import PdfReader
import docx
import pandas as pd
import pytesseract
from PIL import Image

# Load trained pipeline (includes both vectorizer and classifier)
model = joblib.load("model.pkl")

# ---------- Extract Text Functions ----------
def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([para.text for para in doc.paragraphs])

def extract_text_from_doc(file_path):
    # Fallback: try using python-docx (only works if .doc is really .docx)
    try:
        return extract_text_from_docx(file_path)
    except:
        return ""  # For true .doc files you’d need textract/win32com

def extract_text_from_excel(file_path):
    text = ""
    try:
        df = pd.read_excel(file_path, sheet_name=None)  # All sheets
        for sheet, data in df.items():
            text += " ".join(data.astype(str).fillna("").values.flatten())
    except Exception as e:
        print(f"Excel parsing error: {e}")
    return text

def extract_text_from_image(file_path):
    try:    
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Image parsing error: {e}")
        return ""

# ---------- Main Classifier ----------
def classify_document(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    text = ""
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".docx"]:
        text = extract_text_from_docx(file_path)
    elif ext in [".doc"]:
        text = extract_text_from_doc(file_path)
    elif ext in [".xls", ".xlsx"]:
        text = extract_text_from_excel(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        text = extract_text_from_image(file_path)
    elif ext in [".txt"]:
        text = extract_text_from_txt(file_path)
    else:
        print(f"Unsupported file format: {ext}")
        return None

    if not text.strip():
        return "No readable text found"

    # Use the pipeline to predict (includes vectorizer)
    prediction = model.predict([text])
    return prediction[0]

# ---------- Run ----------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python classify.py <document>")
    else:
        file_path = sys.argv[1]
        doc_type = classify_document(file_path)
        print(f"Predicted Document Type: {doc_type}")
