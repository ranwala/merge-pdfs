# 📄 PDF Merger Web App

A simple and user-friendly **Streamlit** web application that allows users to upload multiple PDF files and merge them into a single downloadable PDF. This project uses **PyPDF2** for merging PDFs and **Streamlit** for building the web interface.

---

## 🚀 Features

* Upload multiple PDF files
* Preview merged PDF directly in the browser
* Provide a custom output filename
* Download the merged PDF
* Error handling for corrupted or invalid files

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **Streamlit** – frontend UI
* **PyPDF2** – PDF merging
* **io.BytesIO** – in-memory file handling

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ranwala/merge-pdfs.git
cd pdf-merger-app
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

---

## 🔧 How It Works

1. User uploads PDF files through Streamlit's file uploader
2. Files are passed to `merge_pdfs()` function in `backend.py`
3. PyPDF2 merges the PDFs into a single `BytesIO` object
4. The merged PDF is displayed with `st.pdf`
5. User enters an output filename and downloads the final file

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions for improvements, feel free to open an issue.

---
