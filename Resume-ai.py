!pip install transformers
!pip install gitpython
!pip install python-docx
!pip install PyPDF2
!pip install torch
!pip install opencv-python-headless
!pip install speechrecognition
!pip install pyyaml==5.1
!pip install google-api-python-client
!pip install sklearn
!pip install PyGithub
!pip install requests
!pip install google-api-python-client
!pip install google-auth-httplib2
!pip install google-auth-oauthlib

from docx import Document
import docx
import PyPDF2
from transformers import BertTokenizer, BertModel
import torch
import cv2
import speech_recognition as sr
from github import Github
import requests
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

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

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

def evaluate_skills(job_description_embeddings, resume_embeddings):
    similarity_score = cosine_similarity(job_description_embeddings, resume_embeddings)
    return similarity_score[0][0]

def fetch_coding_questions():
    coding_questions = [
        {
            "id": 1,
            "question": "Write a function to add two numbers.",
            "difficulty": "easy"
        },
        {
            "id": 2,
            "question": "Implement a binary search algorithm.",
            "difficulty": "medium"
        },
        {
            "id": 3,
            "question": "Find the shortest path in a graph using Dijkstra's algorithm.",
            "difficulty": "hard"
        }
    ]
    return coding_questions

def fetch_collaborative_skill_assessments():
    collaborative_assessments = [
        {
            "id": 1,
            "scenario": "You are part of a team working on a project with a tight deadline. A team member is consistently late with their tasks. How do you handle the situation?",
            "difficulty": "medium"
        },
        {
            "id": 2,
            "scenario": "During a team meeting, two members have a disagreement on the approach to solve a problem. How do you facilitate a resolution?",
            "difficulty": "hard"
        },
        {
            "id": 3,
            "scenario": "Your team is tasked with developing a new feature for a product. How do you ensure that all team members' ideas are considered and integrated into the final solution?",
            "difficulty": "easy"
        }
    ]
    return collaborative_assessments

def check_github_plagiarism(project_text):
    g = Github("your_github_token")
    repos = g.search_repositories(query=project_text)
    return repos.totalCount > 0

def check_google_plagiarism(project_text):
    api_key = "your_google_api_key"
    cx = "your_search_engine_id"
    search_url = f"https://www.googleapis.com/customsearch/v1?q={project_text}&key={api_key}&cx={cx}"
    response = requests.get(search_url)
    results = response.json()
    return len(results['items']) > 0

def monitor_exam_integrity():
    cam = cv2.VideoCapture(0)
    recognizer = sr.Recognizer()
    
    while True:
        ret, frame = cam.read()
        cv2.imshow('Exam Monitoring', frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 1:
            print("Multiple faces detected!")
        
        with sr.Microphone() as source:
            print("Listening for unusual sounds...")
            audio = recognizer.listen(source)
            try:
                speech_text = recognizer.recognize_google(audio)
                print(f"You said: {speech_text}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()

def download_file(file_id, destination):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=credentials)

    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f'Download {int(status.progress() * 100)}.')

    fh.close()

def fetch_document_from_drive(file_id, file_type):
    destination = f'/tmp/{file_id}.{file_type}'
    download_file(file_id, destination)
    if file_type == 'pdf':
        return read_pdf(destination)
    elif file_type == 'docx':
        return read_word(destination)
    else:
        raise ValueError("Unsupported file type")

def evaluate_candidate(resume_file_id, resume_file_type, job_desc_file_id, job_desc_file_type, project_texts, code_sample, scenario_answers):
    resume_text = fetch_document_from_drive(resume_file_id, resume_file_type)
    job_description = fetch_document_from_drive(job_desc_file_id, job_desc_file_type)
    
    resume_embeddings = get_bert_embeddings(resume_text)
    job_description_embeddings = get_bert_embeddings(job_description)
    
    coding_questions = fetch_coding_questions()
    collaborative_assessments = fetch_collaborative_skill_assessments()
    
    plagiarism_scores = [check_github_plagiarism(project) or check_google_plagiarism(project) for project in project_texts]
    max_plagiarism_score = max(plagiarism_scores) if plagiarism_scores else 0
    
    coding_test_result = "Assume coding test result"
    collaborative_skills_result = "Assume collaborative skills result"
    skill_evaluation_score = evaluate_skills(job_description_embeddings, resume_embeddings)
    
    monitor_exam_integrity()
    
    return {
        'coding_questions': coding_questions,
        'collaborative_assessments': collaborative_assessments,
        'max_plagiarism_score': max_plagiarism_score,
        'coding_test_result': coding_test_result,
        'collaborative_skills_result': collaborative_skills_result,
        'skill_evaluation_score': skill_evaluation_score
    }

resume_file_id = 'your-resume-file-id'
resume_file_type = 'pdf'  
job_desc_file_id = 'your-job-desc-file-id'
job_desc_file_type = 'docx'  
project_texts = ["Sample project description 1", "Sample project description 2"]
code_sample = "def add(a, b): return a + b"
scenario_answers = ["Answer to scenario 1", "Answer to scenario 2"]

candidate_evaluation = evaluate_candidate(resume_file_id, resume_file_type, job_desc_file_id, job_desc_file_type, project_texts, code_sample, scenario_answers)
print(candidate_evaluation)
