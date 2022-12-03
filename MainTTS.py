# Import the required module for text 
# to speech conversion
from gtts import gTTS
from googletrans import Translator, constants
from pprint import pprint
# This module is imported so that we can 
# play the converted audio
import os

#translator
dest = input("Please enter the desired destination language in 2 character format (like 'en' for english or 'fr' for french): ")
original = input("Please enter the text to be translated: ")
translator = Translator()
translation = translator.translate(original, dest)
mytext = translation.text
#print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print(translation.text)
#Text to speech 
myobj = gTTS(text=mytext, lang=dest, slow=False)

myobj.save("Translation.mp3")
  
os.system("start Translation.mp3")


