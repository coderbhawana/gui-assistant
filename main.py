# Libraries 
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pyjokes
import pywhatkit as kit
import time
from plyer import notification
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, BOTH, SUNKEN
from PIL import Image,ImageTk
from threading import Thread
import requests
import ecapture as ec
import json
import subprocess as sp
import sys
import pyautogui


# Constants for custom styling
BG_COLOR = "#D2C6E2"
BUTTON_COLOR = "#F9F4F2"
BUTTON_FONT = ("Arial", 14, "bold")
BUTTON_FOREGROUND = "black"
HEADING_FONT = ("white", 24, "bold")
INSTRUCTION_FONT = ("Helvetica", 14)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def stop_voice_assistant():
    global stop_flag
    speak("Stopping the Voice Assistant.")
    stop_flag = True
    
def start_voice_assistant():
    global stop_flag
    wishMe()
    perform_task()
    stop_flag = False  # Reset the flag to False when starting the voice assistant
    
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def get_news():
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=34c6bf17ef8c4fdd86e7c815fcb16d5d"
    response = requests.get(url)
    data = json.loads(response.text)
    articles = data["articles"]
    for article in articles:
        title = article["title"]
        source = article["source"]["name"]
        speak(f" {title}")
        print(f"{source} - {title}")
        
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\bhawa\\OneDrive\\Pictures\\Screenshots\\images.png")

def open_cmd():
    os.system('start cmd')

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


entry = None
stop_flag = False

def wishMe():
    global entry
    x = entry.get()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 5:
        speak(f"Good Night! sleep tight.{x}")
        print(f"Good Night! sleep tight.{x}")
    elif 6 <= hour < 12:
        speak(f"Good Morning!{x}")
        print(f"Good Morning!{x}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon!{x}")
        print(f"Good Afternoon!{x}")
    else:
        speak(f"Good Evening!{x}")
        print(f"Good Evening!{x}")

    speak(f"I am iris. Please tell me how may I help you {x}")
    print(f"I am IRIS. Please tell me how may I help you {x}")

def takeCommand():
    # It takes microphone input from the user and returns string output

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        speak("say something")
        recognizer.pause_threshold = 0.8
        recognizer.energy_threshold = 5000
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for 1 second of ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return 'None'
    return query

def perform_task():
    global stop_flag
    while not stop_flag:
        query = takeCommand().lower()  # Converting user query into lower case
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print("According to Wikipedia..")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation error (when the search term has multiple possible meanings)
                print(f"There are multiple meanings for '{query}'. Please be more specific.")
                speak(f"There are multiple meanings for '{query}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found error (when the search term does not match any Wikipedia page)
                print(f"'{query}' does not match any Wikipedia page. Please try again.")
                speak(f"'{query}' does not match any Wikipedia page. Please try again.")
        
        
        elif 'play' in query:
            song = query.replace('play', "")
            speak("Playing " + song)
            print(f"playing {song}")
            kit.playonyt(song)
                   
            
        elif 'open youtube' in query:
            speak(f"Here you go to Youtube\n")
            webbrowser.open("https://youtube.com")
        elif 'close youtube' in query:
            speak("Here you go to close youtube\n")
            os.system("TASKKILL /F /im Chrome.exe")
            
            
        elif 'open chatgpt' in query:
            speak("Here you go to chatgpt\n")
            webbrowser.open("https://chat.openai.com/")
        elif 'close chatgpt' in query:
            speak("Here you go to close chatgpt\n")
            os.system("TASKKILL /F /im Chrome.exe")
            
            
        elif 'open myntra' in query:
            speak("Here you go to myntra\n")
            webbrowser.open("https://myntra.com/")
        elif 'close myntra' in query:
            speak("Here you go to close myntra\n")
            os.system("TASKKILL /F /im Chrome.exe")
            

        elif 'facebook' in query:
            speak("Here you go to facebook\n")
            webbrowser.open('https://www.facebook.com/')
        elif 'close facebook' in query:
            speak("Here you go to close facebook\n")
            os.system("TASKKILL /F /im Chrome.exe")
            

        elif 'open instagram' in query:
            speak("Here you go to instragram\n")
            webbrowser.open('https://www.instagram.com/')
        elif 'close instragram' in query:
            speak("Here you go to close instragram\n")
            os.system("TASKKILL /F /im Chrome.exe")   
            
            
        elif 'search' in query:
            s = query.replace('search', '')
            kit.search(s)
            
        elif "news" in query:
            speak("okay i will search for you")
            print("okay i will search for you")
            speak("Here you go to news\n")
            get_news()

        elif "take a photo" in query:
            speak("Here you go to take your photo \n")
            ec.capture(0, "robo camera", "img.jpg")
            
        elif 'open dominos' in query:
            speak("Here you go to dominos\n")
            webbrowser.open("https://www.dominos.co.in/")
        elif 'close dominos' in query:
            speak("here you go to dominos\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open flipkart' in query:
            speak("Here you go to flipkart\n")
            webbrowser.open("https://flipkart.com")
        elif 'close flipkart' in query:
            speak("here you go to flipkart\n")
            os.system("TASKKILL /F /im Chrome.exe")
            
        elif 'open google' in query:
            speak("Here you go to google\n")
            webbrowser.open("https://google.com")
        elif 'close google' in query:
            speak("here you go to google\n")
            os.system("TASKKILL /F /im Chrome.exe")
            
        elif 'open camera' in query:
            speak("Here you go to camera\n")
            open_camera()
        
        elif "screenshot" in query:
            speak("Here you go to take screenshot\n")
            screenshot()
            speak("I've taken screenshot, please check it in the folder.")
            print("I've taken screenshot, please check it in the folder.")    
            
        elif 'open command prompt' in query or 'open cmd' in query:
            speak("Here you go to cmd\n")
            open_cmd()
             
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {str_time}")
            print(f"the time is {str_time}")
            
        elif 'the date' in query:
            day = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            speak("The current date is " + str(day) + str(month) + str(year))
            print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                speak(month)
                print(month)
            tell_month()
        
        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                speak(day)
                print(day)
            tell_day()
      
        elif 'open code' in query:
            code_path = "C:\\Users\\bhawa\\OneDrive\\Desktop\\gui assistant\\main.py"
            os.startfile(code_path)
            
        elif "advice" in query:
            speak(f"Here's an advice for you")
            print(f"Here's an advice for you")

            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen.")
            print("For your convenience, I am printing it on the screen.")
            print(advice)

        elif "jokes" in query:
            speak(f"Hope you like this one")
            print("Hope you like this one")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            print("For your convenience, I am printing it on the screen.")
            print(joke)
            


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))
            
        elif "send a whatsapp message" in query:
            speak("Here you go to send whatsapp message\n")
            speak('On what number should I send the message? Please enter in the console: ')
            print('On what number should I send the message? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message? please enter your message")
            print("What is the message? please enter your message")
            message = input("Enter your message: ")
            send_whatsapp_message(number, message)
            speak("I've sent the message.")
            print("I've sent the message.")

        elif 'exit' in query:
            speak("Thanks for giving your time")
            stop_voice_assistant()
            
        else:
            speak("Sorry, I didn't understand that. Could you please repeat?")
            print("Sorry, I didn't understand that. Could you please repeat?")




def main():
    # Create the main GUI window
    root = tk.Tk()
    root.title("IRIS - Voice Assistant")
    root.geometry("700x700")
    root.configure(bg=BG_COLOR)
    
    def on_button_click():
        global stop_flag
        if not stop_flag:
            stop_flag = False  # Reset the flag to False when starting the voice assistant
            Thread(target=start_voice_assistant).start()
        else:
            stop_voice_assistant()
            
            
   # Load and set the background image
    background_image = Image.open("C:\\Users\\bhawa\\OneDrive\\Desktop\\gui assistant\\wallpaperflare.com_wallpaper.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = ttk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    f1 = ttk.Frame(root)
    f1.pack(pady=100)  # Add some padding to the frame to center it vertically

    image2 = Image.open("C:\\Users\\bhawa\\OneDrive\\Desktop\\gui assistant\\p.jpg")
    resized_image = image2.resize((120, 120))
    p2 = ImageTk.PhotoImage(resized_image)
    l2 = ttk.Label(f1, image=p2, relief=SUNKEN)
    l2.pack(side="top", fill="both")

    # Heading
    heading_label = ttk.Label(root, text="Voice Assistant", font=HEADING_FONT, background=BG_COLOR)
    heading_label.pack(pady=20)

    global entry
    f1 = ttk.Frame(root)
    f1.pack()
    l1 = ttk.Label(f1, text="Enter Your Name", font=INSTRUCTION_FONT, background=BG_COLOR)
    l1.pack(side=LEFT, fill=BOTH)
    entry = ttk.Entry(f1, width=30)
    entry.pack(pady=10)

    # Instruction
    instruction_label = ttk.Label(root, text="Click the button below to start the Voice Assistant.", font=INSTRUCTION_FONT, background=BG_COLOR)
    instruction_label.pack(pady=10)


    # Create and place a button on the GUI
    button = ttk.Button(root, text="Start Voice Assistant", command=on_button_click, style="VoiceAssistant.TButton")
    button.pack(pady=20)

    # Style the button
    style = ttk.Style(root)
    style.configure("VoiceAssistant.TButton", font=BUTTON_FONT, background=BUTTON_COLOR, foreground=BUTTON_FOREGROUND)

    # Run the GUI main loop
    root.mainloop()


if __name__ == "__main__":
    main()















