import speech_recognition as sr 
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
	print("audioString")
	tts = gTTS(text = audioString, lang = 'en')
	tts.save("audio.mp3")
	os.system("mpg321 audio.mp3")

def recordAudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something")
		audio = r.listen(source)

	data = ""
	try:
		data = r.recognize_google(audio)
		print("U said:" + data)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	return data

def jarvis(data):
	if "how are you" in data:
		speak("I am fine")

	if "what time is it" in data:
		speak(ctime())

	if "where is" in data:
		data = data.split(" ")
		location = data[2]
		speak("Hold on, I will show you where" + location + "is.")
		os.system("firefox https://google.nl/maps/place/" + location + "/&amp;")

	time.sleep(2)
	speak("Hi, what can I do for you?")
	while(1):
		data = recordAudio()
		jarvis(data)