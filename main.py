import speech_recognition as sr  #pip install speechrecognition pyaudio
import webbrowser  #
import pyttsx3
import my_requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommnad(c):
    print(c)
    if c.lower().startswith("play") or c.lower().startswith("open"):
        video=c.lower().split(" ")[1:]
        content=""
        for i in video:
            content+=i
            content+=" "
        print(content)
        link=my_requests.my_videos[content.strip()]
        print(link)
        webbrowser.open(link)

if __name__=="__main__":
    speak("Initializing Jarvis!!")
    while True:
        #listen for the wake word: Jarvis
        #Obatin audio from the microphone
        r=sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Aniket!")
                #listen for word
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommnad(command)

        except Exception as e:
            print("Error; {0}".format(e))