import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
from transformers import pipeline
import pyjokes
import random
import threading
import hud_ui
import datetime

# def processcommand(c):
  
#     c = c.lower()

#     # --- TIME ---
#     if "time" in c:
#         now = datetime.datetime.now().strftime("%I:%M %p")
#         speak(f"The time is {now}")
#         return

#     # --- DATE ---
#     elif "date" in c:
#         today = datetime.datetime.now().strftime("%d %B %Y")
#         speak(f"Today's date is {today}")
#         return

#     # --- DAY ---
#     elif "day" in c:
#         day = datetime.datetime.now().strftime("%A")
#         speak(f"Today is {day}")
#         return
    
# # Other commands...


def run_jarvis():
     jarvis_loop()

engine =  pyttsx3.init() #new
engine.setProperty("rate",175) #new

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
r.energy_threshold = 300  #new
r.dynamic_energy_ratio = 1.5 #new

# engine = pyttsx3.init()
joke = pyjokes.get_joke()
print(joke)

def tell_hindi_joke():
    jokes = random.choice("tell_hindi_joke")
    speak(jokes)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def aiprocess(c):
   chatbot = pipeline("text-generation", model= "gpt2")
   prompt = "command" 

   response =chatbot(prompt, truncation=True, max_length = 70,num_return_sequences = 1,temperature = 0.8)
   return(response[0]["generated_text"])


def processcommand(c):
    if "open google" in c.lower():
      webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
      webbrowser.open("https://Youtube.com")

    elif "open facebook" in c.lower():
      webbrowser.open("https://Facebook.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif c.lower().startswith("start joke"):
         speak(hindi_jokes)

    elif "hindi joke" in c:
            c.lower().startswith("start joke")
            hindi_jokes  = c.lower().split(" ")[0]
            tell_hindi_joke()

    else:
       output = aiprocess(c)
       speak(output)

def jarvis_loop():
  speak("Hello, system online.")
  

  while True:
    # listen for the wake word
    # obtain audio for the microphone
    r = sr.Recognizer()
    print("Recognizing...")

    try:
      with sr.Microphone() as source:
          print("listening...")
          audio = r.listen(source,timeout=5,phrase_time_limit=4)

      word = r.recognize_google(audio) 

      if (word.lower() == "jarvis"):
        speak("Yay,I am here")
        #Listen for command
        with sr.Microphone() as source: 
         print("jarvis Active....")
         audio = r.listen(source)
        command = r.recognize_google(audio)

        processcommand(command)
        aiprocess(command)
        tell_hindi_joke(command)
  

    except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
 
    except Exception as e:
      print("error; {0}".format(e))

  # ... baaki AI logic ...

if __name__ == "__main__":

  #   # Start HUD in MAIN thread (required)
  #   hud_ui.start_hud() 

  # #START HUD IN THREAD
  #   hud_thread = threading.Thread(target=hud_ui.start_hud)
  #   hud_thread.daemon = True
    

    # Keep Main thread Alive
    jarvis_thread = threading.Thread(target= jarvis_loop)
    jarvis_thread.daemon = True
    jarvis_thread.start()
    
    hud_ui.start_hud()

    