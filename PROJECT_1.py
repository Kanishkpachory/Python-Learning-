import speech_recognition as sr
import webbrowser
import pyttsx3

recoginzer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__" :
    speak("Initializing Jarvis..... ")
    while True :
        #Listen for the wake word "jarvis "
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listining...")
            audio = r.listen(source)

        

        # recognize speech using google
        print("recognizing...")
        try:
           commmand = r.recognize_google (audio)
           print(commmand)
        
        except Exception as e:
           print("Error ; {0}".format(e))
