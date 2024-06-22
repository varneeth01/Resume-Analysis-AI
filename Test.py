import cv2
import speech_recognition as sr

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

monitor_exam_integrity()
