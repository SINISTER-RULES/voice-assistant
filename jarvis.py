import speech_recognition as sr     #for speech recognition
import pyttsx3                      #for text to speech
import os
import playonyoutube
import wikipedia                    #for info from wikipedia
import tkinter   
import webbrowser as wb  
import urllib.request           
from tkinter import filedialog      #for the dialog box to select file
import pyautogui                    #for the image to text converter
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

tk = tkinter.Tk()
tk.withdraw()
engine = pyttsx3.init()
engine.setProperty('rate',125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def enginespeak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


try:
    html = urllib.request.urlopen("https://google.com", timeout=5)
except:
    err = "No Internet Connection. Please try again."
    print(err)
    enginespeak(err)
    os.system('cls')
    exit()


r = sr.Recognizer()

def speak(text):
    if 'play' in text:
        enginespeak("playing")
        text = text.replace('play', '')
        playonyoutube.youtube(text)
        os.system('cls')
        quit()
    elif 'who are you' in text:
        enginespeak("Hi my name is Xander, I was created by Samarth Joseph.")
    elif 'search' in text:
        text=text.replace('search ', '')
        print("Showing results..")
        enginespeak("Showing results")
        text = text.replace(' ', '+')
        wb.open("https://www.google.com/search?q="+text)
        os.system('cls')
        quit()
    elif 'who is'in text:
        text=text.replace('who is','')
        try:
            info = wikipedia.summary(text, sentences=2)
            print(info)
            engine.setProperty('rate',175)
            enginespeak(info)
            engine.setProperty('rate',125)
        except:
            print("Couldn't find the person you were looking for!")
            enginespeak("could not find the person you were looking for")
    elif 'recognise' in text:
        image = filedialog.askopenfilename()
        img = Image.open(image)
        output = pytesseract.image_to_string(img)
        print(output)
        enginespeak("Do you want me to read it?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening for answer...')
            ans = r.listen(source)
            t = r.recognize_google(ans)
            if("yes") in t:
                enginespeak('the text in the image is'+output)
            else:
                return
        os.system('cls')
    elif 'hello' in text:
        print("Hi, how are you?!")
        enginespeak("hi, how are you?")
    else:
        print("Sorry, could not understand what you said!")
        enginespeak("Sorry, could not understand what you said, Please speak again.")

while True:
    print("\nCommands are:\n")
    print("1. Play _____\n2. Who are you?\n3. Search _____\n4. Hello\n5. Recognise text in image\n")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening......")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            speak(text)
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said!")
            enginespeak("Sorry, could not understand what you said")

                
    os.system('cls')
    print("Do you want to give another command?\n")
    enginespeak("Do you want to give another command?")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        try:
            if 'yes' in text:
                os.system('cls')
                continue
            else:
                os.system('cls')
                break
        except sr.UnknownValueError:
            os.system('cls')
            break

os.system('cls')
print("Thank You!!")