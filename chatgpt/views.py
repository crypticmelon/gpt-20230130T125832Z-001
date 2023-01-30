from django.shortcuts import render
from django.http import HttpResponseRedirect
import openai
import pyttsx3
import speech_recognition as speech

# Create your views here.




def index(request):
    response = ""
    engine = pyttsx3.init()
    has_set = False
    newVoiceRate = 60
    engine.setProperty('rate',newVoiceRate)
        
    if (request.GET.get('mybtn') and has_set == False):
            has_set = True
            r = speech.Recognizer()
            with speech.Microphone() as source: 
                print("Listening...")
                r.pause_threshold = 1
                print("Recognizing...")   
                audio = r.listen(source)
                query = r.recognize_google(audio, language ='en-in')
            openai.api_key = "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"
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )
            if engine._inLoop:
                engine.inLoop = False
            engine.say(response.choices[0].text)
            engine.runAndWait()
            print(response.choices[0].text)
            return render(request, "chatgpt/index.html", {
                "response" : response.choices[0].text
            })
    elif (request.GET.get('mybtn') and has_set == True):
        print("Hi")
    return render(request, "chatgpt/index.html")
