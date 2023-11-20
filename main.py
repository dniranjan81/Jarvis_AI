import speech_recognition as sr
import os
import time
import pyttsx3
import webbrowser
import datetime
import openai
import random
from config import apikey
from newsapi import NewsApiClient
import pyowm

chatStr = ""
api_key = 'fb1f6d7dcd334ead9fd153ed41158ad3'
api_key1 = '838d332c63a1e93e76875893de429005'
newsapi= NewsApiClient(api_key=api_key)
owm= pyowm.OWM(api_key1)

def get_weather(city):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temperature = weather.temperature('celsius')["temp"]
    status = weather.status
    return f"The current weather in {city} is {status} with a temperature of {temperature}°C."

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"niranjan: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Niranjan said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
            print("Listening...")
            new_query = takeCommand()
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                     ["google", "https://www.google.com"], ]
            for site in sites:
                if f"Open {site[0]}".lower() in new_query.lower():
                    say(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])
            # todo: Add a feature to play a specific song
            if "open music" in new_query:
                musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
                os.system(f"open {musicPath}")
            elif "the time" in new_query:
                musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir time is {hour} bajke {min} minutes")
            elif "open facetime".lower() in new_query.lower():
                os.system(f"open /System/Applications/FaceTime.app")
            elif "news" in new_query.lower():
                say("Sure, fetching the latest news headlines for you.")
                top_headlines = newsapi.get_top_headlines(country='us', language='en', page_size=5)
                articles = top_headlines['articles']
                for article in articles:
                    say(article['title'])
                    say(article['description'])
            elif "weather" in new_query.lower():
                say("Sure, fetching the weather information.")
                say("Please tell me the name of your city")
                city = takeCommand()  # You can replace this with voice input using speech recognition
                say(f'did you mean:{city}?')
                query = ''
                try:
                    weather_info = get_weather(city)
                    say(weather_info)
                except:
                    say('sorry something went wrong. Please try again')
                    query = ''
            elif "open pass".lower() in new_query.lower():
                os.system(f"open /Applications/Passky.app")
            elif "Using artificial intelligence".lower() in new_query.lower():
                ai(prompt=new_query)
            elif "Jarvis Quit".lower() in new_query.lower():
                exit()
            elif "reset chat".lower() in new_query.lower():
                chatStr = ""
            elif "Jarvis Quit".lower() in new_query.lower() or "stop" in new_query.lower():
                say("Goodbye! Exiting Jarvis.")
                exit()

            else:
                print("Chatting...")
                query = ''
                chat(new_query)




        # say(query)
