import streamlit as st  # Streamlit for UI
import PyPDF2  # Extract text from PDFs
import pandas as pd  # Handle data
import matplotlib.pyplot as plt  # For visualization
from sklearn.feature_extraction.text import TfidfVectorizer  # Convert text into numerical features
from sklearn.metrics.pairwise import cosine_similarity  # Measure text similarity

# Streamlit page configuration
st.set_page_config(page_title="Plagiarism Checker", layout="wide")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = "".join([page.extract_text() + "\n" for page in pdf_reader.pages])
    return text

# Function to check plagiarism using TF-IDF and Cosine Similarity
def check_plagiarism(input_text, database_texts):
    corpus = [input_text] + database_texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0] * 100
    max_similarity = max(similarity_scores)
    
    # Simulating 100% plagiarism detection for Google content
    if max_similarity > 90:
        max_similarity = 100
    
    return max_similarity, similarity_scores

# Sample database of stored documents (can be replaced with a real database)
database_texts = [
    "This is a sample document stored in the system.",
    "Academic writing must be original and free of plagiarism.",
    "Machine learning is an interesting field of study.",
    "Plagiarism is a serious ethical violation in research and academia."
]

# UI Title
st.title("📄 Advanced Plagiarism Checker")

# File Upload and Text Input
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    
with col2:
    text_input = st.text_area("Or Paste Your Text Here:")

# Extract text from uploaded file
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text_input = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        text_input = uploaded_file.read().decode("utf-8")

# Check Plagiarism Button
if st.button("🔍 Check Plagiarism"):
    if text_input:
        plagiarism_score, similarity_scores = check_plagiarism(text_input, database_texts)
        st.subheader(f"Plagiarism Score: {plagiarism_score:.2f}%")
        
        if plagiarism_score >= 50:
            st.warning("⚠️ High similarity detected. Consider revising your text.")
        else:
            st.success("✅ Your text is mostly original.")
        
        # Chart Visualization
        fig, ax = plt.subplots()
        ax.bar(range(len(similarity_scores)), similarity_scores, color='skyblue')
        ax.set_xticks(range(len(similarity_scores)))
        ax.set_xticklabels([f"Doc {i+1}" for i in range(len(similarity_scores))], rotation=45)
        ax.set_ylabel("Similarity (%)")
        ax.set_title("Similarity Scores with Stored Documents")
        st.pyplot(fig)
    else:
        st.warning("⚠️ Please enter or upload text to check for plagiarism.")















































# import streamlit as st  # Streamlit for web UI
# import PyPDF2  # Extract text from PDFs
# import pandas as pd  # Handle data (optional)
# from sklearn.feature_extraction.text import TfidfVectorizer  # Convert text into numerical features
# from sklearn.metrics.pairwise import cosine_similarity  # Measure text similarity

# # Streamlit page configuration
# st.set_page_config(page_title="Plagiarism Checker", layout="centered")

# # Function to extract text from a PDF file
# def extract_text_from_pdf(pdf_file):
#     pdf_reader = PyPDF2.PdfReader(pdf_file)  # Read PDF file
#     text = ""  # Store extracted text
#     for page in pdf_reader.pages:  # Loop through each page
#         text += page.extract_text() + "\n"  # Append text from each page
#     return text

# # Function to check plagiarism using TF-IDF and Cosine Similarity
# def check_plagiarism(input_text, database_texts):
#     corpus = [input_text] + database_texts  # Combine input text with database documents
#     vectorizer = TfidfVectorizer()  # Initialize TF-IDF vectorizer
#     tfidf_matrix = vectorizer.fit_transform(corpus)  # Convert texts into numerical format
    
#     similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])  # Compute similarity
#     plagiarism_percentage = max(similarity_scores[0]) * 100  # Get highest similarity score

#     return plagiarism_percentage  # Return percentage similarity

# # 🏠 App Title
# st.title("📄 Plagiarism Checker")

# # 📤 User File Upload or Text Input
# uploaded_file = st.file_uploader("Upload a TXT or PDF file", type=["pdf", "txt"])
# text_input = st.text_area("Or Paste Your Text Here:")

# # Sample database of stored documents (can be replaced with a real database)
# database_texts = [
#     "This is a sample document stored in the system.",
#     "Academic writing must be original and free of plagiarism.",
#     "Machine learning is an interesting field of study."
# ]

# # Extract text if file is uploaded
# if uploaded_file:
#     if uploaded_file.type == "application/pdf":
#         text_input = extract_text_from_pdf(uploaded_file)  # Extract text from PDF
#     elif uploaded_file.type == "text/plain":
#         text_input = uploaded_file.read().decode("utf-8")  # Read text from TXT file

# # 🔍 Check Plagiarism Button
# if st.button("🔍 Check Plagiarism"):
#     if text_input:
#         plagiarism_score = check_plagiarism(text_input, database_texts)  # Call function to check plagiarism
#         st.subheader(f"Plagiarism Score: {plagiarism_score:.2f}%")  # Display plagiarism percentage

#         # 🚨 Warning for high plagiarism
#         if plagiarism_score > 50:
#             st.warning("⚠️ High similarity detected. Consider revising your text.")
#         else:
#             st.success("✅ Your text is mostly original.")
#     else:
#         st.warning("⚠️ Please enter or upload text to check for plagiarism.")
