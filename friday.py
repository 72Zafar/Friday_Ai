import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def data_time():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning Sir")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")    

    speak("I am Friday Ai Sir. Please tell me how may I help you ")      

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print ("Recognizing...")
        quary = recognizer.recognize_google(audio, language='en-US')
        print (f"User said{quary} \n")
        return quary .lower()
    

    except Exception as e:
        print (e)    
        print ("say that again please...")
        return "None"    



if __name__ == "__main__":
    data_time()
    # while True:
    query =  take_command()

    if "wikipedia" in query:
        speak("Seraching wikipedia... ")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia")
        print (results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')  

    elif 'open google' in query:
        webbrowser.open('google.com')     

    elif 'open whatsapp' in query:
        webbrowser.open("whatsapp")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\hp 840 G3\\Music'
        songs = os.listdir(music_dir)  
        print (songs) 
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        srtTime = datetime.datetime.now().srtTime("%H:%M:%S")
        speak(f"Sir the time is{srtTime}")




