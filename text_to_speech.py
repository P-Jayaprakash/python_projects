# Import the required module for text 

from gtts import gTTS 

 
# to play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = 'your text is converted to speech!'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 

myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 

myobj.save("my.mp3") 

# Playing the converted file 
os.system("mpg321 my.mp3") 
