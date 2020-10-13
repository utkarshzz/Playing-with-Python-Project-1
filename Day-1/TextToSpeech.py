"""
Python Code by using pyttsx3 that converts Text to speech 
using pyttsx3
Created on Tue Oct 13 10:25:47 2020
@author: Gyan Krishna

install the following packages:-
pip install pyttsx3
pip install gTTS (for second alternative)
"""

import pyttsx3

engine = pyttsx3.init()

# speaking rate
engine.setProperty('rate', 150)

# speaking volume - volume b/w 0 and 1
engine.setProperty('volume', 0.7)

# voice selection:- 0 - male, 1 - female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# gathering current volume and rate of speech
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')

print('volume = ', volume)
print('rate of play = ', rate)

engine.say("hello world")
engine.runAndWait()

# #Python Code by using pyttsx3 that converts Text to speech
# #using gtts <google text to speech>

# from gtts import gTTS
# from playsound import playsound

# SampleText = "hello world"
# aud = gTTS(text = SampleText,lang = 'en',slow = False)
# aud.save("hello.mp3")
# playsound("hello.mp3")
