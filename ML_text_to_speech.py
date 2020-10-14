#!/usr/bin/env python
# coding: utf-8

# In[2]:


from gtts import gTTS


# In[3]:


from playsound import playsound


# In[4]:


get_ipython().system('pip install playsound')


# In[5]:


from playsound import playsound


# In[15]:


text_val = 'Guess whos back, back again!'
language = 'en'
obj = gTTS(text = text_val, lang = language, slow = False)
obj.save("project3.mp3")
playsound("project3.mp3")


# In[ ]:





# In[ ]:




