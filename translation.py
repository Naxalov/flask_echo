import requests
import json

text = input("입력 하시요: ")

def translate_bot(text):
    
    payload ={
        "q":text,
        "target":"en",
        "key": "AIzaSyD7_2HWvkXkjXZ_9CkPhP8Vp8bSVuJ85mY"
    }


    r = requests.post(url="https://translation.googleapis.com/language/translate/v2", params=payload)
    data =r.text
    data =json.loads(data)
    print("Original:", data["data"]["translations"][0]["translatedText"])


translate_bot(text)

import googletrans

def trans_late(text):
    from googletrans import Translator
    translator = Translator()
    print(translator.translate(text, dest="en").text)
    return translator.translate(text, dest="en").text

trans_late(text)
