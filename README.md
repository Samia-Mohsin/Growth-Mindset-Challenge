# 🔍 Plagiarism Checker

A **Streamlit web app** to check for plagiarism using **TF-IDF and Cosine Similarity**. Users can upload PDF/TXT files or paste text to detect similarities against a stored database.

---

## 🚀 Features

- **PDF & Text Input**: Users can upload a PDF/TXT file or directly input text.
- **Plagiarism Detection**: Uses **TF-IDF & Cosine Similarity** to compare input text with stored documents.
- **Similarity Score**: Provides a **plagiarism percentage** based on document comparisons.
- **Graphical Representation**: Bar chart visualization of similarity scores.

---

## 🛠 Installation

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/plagiarism-checker.git
cd plagiarism-checker
```

### **2️⃣ Create a Virtual Environment (Recommended)**

```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

To manually create `requirements.txt`, run:

```bash
pip freeze > requirements.txt
```

Or manually list dependencies:

```
streamlit
PyPDF2
pandas
matplotlib
scikit-learn
```

---

## ▶️ Usage

### **Run the Streamlit App**

```bash
streamlit run app.py
```

This will launch the plagiarism checker in your web browser.

---

## 📂 Project Structure

```
📂 plagiarism-checker
│-- app.py  # Main Streamlit application
│-- sample_texts/  # Directory for sample database texts
│-- requirements.txt  # List of dependencies
│-- README.md  # Project documentation
```

---

## 🚀 Deployment

### **Deploy on Streamlit Cloud**

1. Push your project to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy!

### **Deploy on Render or Hugging Face Spaces**

For **Render**:

1. Create a new web service on [Render](https://render.com/).
2. Select your GitHub repository and choose Python environment.
3. Set `Start Command`: `streamlit run app.py`
4. Deploy 🚀

For **Hugging Face Spaces**:

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces).
2. Select **Streamlit** as the SDK.
3. Upload your code and `requirements.txt`.
4. Deploy! ✅

---

## 💡 Future Improvements

- Support for real-time web searches to detect content from Google.
- Database integration for larger document comparisons.
- Advanced NLP techniques for paraphrase detection.

🔍 **Ensure originality and avoid plagiarism!** 🚀

