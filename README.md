# 📂 eOffice Document Classifier – CDAC Guwahati  

An AI-powered document classification system for **CDAC eOffice**, designed to automatically categorize office documents such as **Indent, Invoice, Bill, Note, and Tender**.  
The system evolves from **text-only classification** to **multimodal document understanding** (text + image + layout), making it suitable for both **digital PDFs** and **scanned documents**.  

---

## ✨ Features
- ✅ Classifies documents into: **Indent, Invoice, Bill, Note, Tender**  
- ✅ Supports **digital text documents (Word/PDF)** and **scanned images**  
- ✅ **OCR integration** for image-heavy/scanned files  
- ✅ **BERT-based text model** (baseline)  
- ✅ **LayoutLM/Donut multimodal model** for structured + scanned docs  
- ✅ Hybrid approach for **cost-optimized deployment**  
- ✅ Extensible to **RAG (Retrieval-Augmented Generation)** for smart document search  

---

## 📂 Project Structure
```bash
eoffice-doc-classifier/
│── data/                # Dataset (synthetic + real CDAC docs)
│   ├── train.csv
│   ├── val.csv
│   └── test.csv
│── models/              # Trained models & checkpoints
│── notebooks/           # Jupyter notebooks for experiments
│── src/                 # Source code
│   ├── preprocessing.py # Data cleaning, OCR pipeline
│   ├── train_text.py    # Training text-only models (BERT, TF-IDF)
│   ├── train_multimodal.py # Training LayoutLM/Donut
│   ├── predict.py       # Inference script
│   └── utils.py
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── app.py               # FastAPI/Flask deployment API
