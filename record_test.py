import speech_recognition as sr

# Recognizer aur microphone initialize karo
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)  # ← Yahan mic index aapke system ke hisaab se set karo

with mic as source:
    print("Adjusting for background noise...")
    r.adjust_for_ambient_noise(source, duration=1)

    print("Recording for 5 seconds... Speak now.")
    audio = r.listen(source, timeout=5)

# Record hua audio file me save karo
with open("test.wav", "wb") as f:
    f.write(audio.get_wav_data())

print("Recording saved as 'test.wav'")
