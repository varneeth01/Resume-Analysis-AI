# Project Overview:
The AI-Driven Resume Analysis and Interview Assistance System is designed to automate and enhance the candidate evaluation process for hiring managers and HR professionals. This system leverages advanced artificial intelligence and machine learning techniques to analyze resumes, evaluate coding and collaborative skills, detect plagiarism in project submissions, and monitor exam integrity during assessments. It provides a comprehensive solution to streamline the recruitment process, ensuring a more efficient and effective candidate evaluation.

# Key Features:

Resume Parsing and Analysis:
- Text Extraction: The system can read and extract text from both Word and PDF resume documents using docx and PyPDF2 libraries.
- NLP Processing: Utilizes BERT (Bidirectional Encoder Representations from Transformers) for extracting and processing textual data from resumes and job descriptions, converting them into embeddings for similarity analysis.
- Skill Matching: Compares the extracted resume data with job descriptions to evaluate the candidate's suitability for the role.

Coding and Collaborative Skill Assessments:
- Fetch Questions: Automatically fetches coding questions and collaborative scenario-based questions from predefined sets.
- Coding Evaluation: Assesses candidates' coding skills by evaluating their responses to coding questions.
- Collaborative Skill Evaluation: Assesses candidates' responses to scenario-based questions to evaluate their collaborative and problem-solving skills.

Plagiarism Detection:
=
- GitHub Plagiarism Check: Uses the GitHub API to check if the project descriptions provided in resumes are plagiarized from existing repositories.
- Google Plagiarism Check: Utilizes Google Custom Search API to detect if project descriptions are copied from online sources.
  
Exam Integrity Monitoring:
- Camera Monitoring: Uses OpenCV to monitor the candidate through a webcam during coding tests to detect multiple faces or unusual activities.
- Speech Recognition: Uses the speech_recognition library to monitor and transcribe audio during exams to detect any unusual sounds or speech that might indicate cheating.
  
Integration with Cloud Services:
- Google Drive Integration: Downloads resumes and job descriptions directly from Google Drive using the Google Drive API.
- Service Account Authentication: Uses Google Service Account for secure authentication and file access.
