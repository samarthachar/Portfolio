import pdfplumber
import os
import pyttsx3

def pdf_to_text(path):
    text = ''
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


text = False
file_path = input("Enter the path to a .pdf or .txt file: ")
if not os.path.isfile(file_path):
    print("That file doesn't exist.")
elif not file_path.lower().endswith('.pdf'):
    print("Unsupported file type. Please upload a .pdf or .txt file.")
else:
    print("File accepted!")
    text = pdf_to_text(file_path)

if text:
    speak_text(text)