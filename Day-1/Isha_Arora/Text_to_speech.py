#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# In[5]:


get_ipython().system('pip install gTTS')
get_ipython().system('pip install playsound')
from gtts import gTTS
#playsound pkg is used to get any sound data from Gtts and save it in a sound file
from playsound import playsound
text_val = 'Hello world out there'
language ='en'
obj = gTTS(text = text_val , lang = language , slow= False)
obj.save("exams.mp3")
playsound("exams.mp3")


# In[ ]:




