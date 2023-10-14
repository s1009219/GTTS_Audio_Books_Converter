#Packages import pip install pyttsx3, pip install PyPDF2, pip install gTTS
import pyttsx3
import PyPDF2
from tkinter.filedialog import *
###from gtts import gTTS

book = askopenfilename()
pdfReader = PyPDF2.PdfReader(book)
number_of_page = len(pdfReader.pages)
print(number_of_page)
page = pdfReader.pages[0]

for num in range(0,number_of_page):
  text = page.extract_text()
  engine = pyttsx3.init()
  engine.setProperty("rate", 2000)
  engine.say(text)
  engine.runAndWait()

"""
#tts = gTTS(text, lang='en')
#tts.save("good.mp3")
#from IPython.display import Audio
#Audio("good.mp3")

#Replace gTTS with pyttsx3
# 初始化
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# 語速控制
rate = engine.getProperty('rate')
engine.setProperty("rate", 2000)
print(rate)
# 音量控制
volume = engine.getProperty('volume')
print(volume)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
# 朗讀
engine.say(text)
engine.runAndWait()"""
