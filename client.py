from transformers import pipeline
import time
from main import speak

def start_jarvis():
    time.sleep(2)  # HUD ready hone ka wait

    speak("Hello sir, Jarvis system online.")
     

chatbot = pipeline("text-generation", model= "gpt2")
prompt = "what is python?"
 

response =chatbot(prompt, truncation=True, max_length = 128,num_return_sequences = 1)
print(response[0]["generated_text"])