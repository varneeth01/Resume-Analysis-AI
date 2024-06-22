!pip install python-docx PyPDF2 transformers torch opencv-python-headless speechrecognition pyyaml==5.1
!pip install python-docx PyPDF2 transformers torch opencv-python-headless speechrecognition pyyaml==5.1
!pip install gitpython google-api-python-client
!pip install python-docx
!pip install PyPDF2

from docx import Document
import PyPDF2

def read_word(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def read_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    full_text = []
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        full_text.append(page.extractText())
    pdf_file.close()
    return '\n'.join(full_text)
