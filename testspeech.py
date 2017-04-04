#Make sure to make a directory to send the transcriptions
#create the transcriptions directory on your machine 
#make sure you have cmusphinx working and the speechrecogniton module installed
import speech_recognition as sr
import os
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_sphinx(audio)
os.system("cd transcriptions")
s = open("spokentext.docx", "w")
r = open("spokentext.docx", "r")
s.write(text)

