import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
   mytext = str(text)
   language = 'hi'
   myobj = gTTS(text = mytext, lang=language, slow=False)
   myobj.save(filename)

# These function returns pydubs audio segment
def mergeAudios(audios):
   combined = AudioSegment.empty()
   for audio in audios:
      combined += AudioSegment.from_mp3(audio)
   return combined

def generateSkeleton():
   audio = AudioSegment.from_mp3('railway.mp3')

   # 1 - Generating krupiy dhayn dey gadi kramank
   start = 3000
   finish = 6000
   audioProcessed = audio[start:finish]
   audioProcessed.export("1_hindi.mp3", format="mp3")

   # 2 - train number
   
   # 3 - train name

   # 4 - Generating thodi he dar ma platform kramank
   start = 11000
   finish = 13000
   audioProcessed = audio[start:finish]
   audioProcessed.export("4_hindi.mp3", format="mp3")

   # 5 - platform number

   # 6 - par arahiha
   start = 14000
   finish = 15000
   audioProcessed = audio[start:finish]
   audioProcessed.export("6_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
   df = pd.read_excel(filename)
   print(df)
   for index, item in df.iterrows():
      # 2 - generating train number and name
      textToSpeech(item['train_no'] + " " + item['from'] + "saa " + item['to'] + " jane wali ", "2_hindi.mp3")
      # 3 - generating train name
      textToSpeech( item['train_name'], "3_hindi.mp3")
      # 5 - generating platform number
      textToSpeech(item['platform'], "5_hindi.mp3")

      audios = [f"{i}_hindi.mp3" for i in range(1,7)]
      announcement = mergeAudios(audios)
      announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == '__main__':
   print("Generating sklleton...")
   generateSkeleton()
   print("Now generating Announcement...")
   generateAnnouncement("announce_hindi.xlsx")