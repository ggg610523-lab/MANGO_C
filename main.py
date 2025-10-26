import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import sys

# Initialize the speech engine (cross-platform)
engine = pyttsx3.init()  # Automatically chooses the correct driver
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Pick the last available voice

# Function to speak
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# Greeting based on the time
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH < 12:
        speak('Good Morning!')
    elif currentH < 18:
        speak('Good Afternoon! should i bomb these bitches')
    else:
        speak('Good Evening!')

# Take voice commands from the user
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak("Sorry sir! I didn't get that. Please type the command.")
        query = input("Command: ")
    except sr.RequestError:
        speak("Sorry, the speech service is down. Please try again later.")
        return ""
    return query.lower()

# Main program
if __name__ == "__main__":
    greetMe()
    speak("Hello Sir, I am your digital assistant chota bheem ")
    speak("How may I help you?")

    commands = {
        'open youtube': 'https://www.youtube.com',
        'open google': 'https://www.google.co.in',
        'open gmail': 'https://www.gmail.com'
    }

    try:
        while True:
            query = myCommand()
            if not query:
                continue

            # Open websites
            executed = False
            for cmd in commands:
                if cmd in query:
                    speak('Okay')
                    webbrowser.open(commands[cmd])
                    executed = True
                    break
            if executed:
                continue

            # Small talk
            if "what's up" in query or "how are you" in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am full of energy']
                speak(random.choice(stMsgs))

            elif "hello" in query:
                speak("Hello Sir!")

            # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    speak(results)
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple options. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I could not find anything on Wikipedia.")

            # Current time
            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            # Exit commands
            elif "nothing" in query or "abort" in query or "stop" in query or "bye" in query:
                speak("Okay")
                speak("Bye Sir, have a good day.")
                sys.exit()

            # Unknown command fallback
            else:
                speak("Sorry Sir, I don't understand that command.")

    except KeyboardInterrupt:
        speak("Exiting. Bye Sir!")
        sys.exit()
