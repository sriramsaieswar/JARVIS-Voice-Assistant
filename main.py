import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia
import time


# ============================================================
# 1. LOGGER SETUP
# ============================================================

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# ============================================================
# 2. SPEECH RECOGNIZER
# ============================================================

recognizer = sr.Recognizer()

# Controls how long JARVIS waits between words
recognizer.pause_threshold = 0.8

# Minimum audio energy required
recognizer.energy_threshold = 300

# Automatically adjust for changing microphone noise
recognizer.dynamic_energy_threshold = True


# ============================================================
# 3. TEXT TO SPEECH
# ============================================================

def speak(text):
    """
    Convert text to speech using Windows SAPI5.

    A new engine is created for every response.
    This avoids pyttsx3 getting stuck after the first response.
    """

    print(f"JARVIS: {text}")

    try:

        engine = pyttsx3.init("sapi5")

        voices = engine.getProperty("voices")

        if len(voices) > 0:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(str(text))
        engine.runAndWait()

        engine.stop()

        del engine

        # Small pause to allow Windows SAPI to release audio
        time.sleep(0.1)

    except Exception as e:

        logging.error(f"TTS Error: {e}")

        print(f"TTS ERROR: {e}")


# ============================================================
# 4. TAKE COMMAND
# ============================================================

def take_command():

    """
    Listen to microphone and convert speech to text.
    """

    with sr.Microphone() as source:

        print("\nListening...")

        try:

            # Adjust to background noise
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            print("Listening timeout.")

            return "none"

        except Exception as e:

            logging.error(f"Microphone Error: {e}")

            print(f"Microphone Error: {e}")

            return "none"


    # --------------------------------------------------------
    # Speech Recognition
    # --------------------------------------------------------

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        query = query.lower().strip()

        print(f"You said: {query}")

        return query


    except sr.UnknownValueError:

        print("I could not understand what you said.")

        speak("Sorry sir, I didn't understand.")

        return "none"


    except sr.RequestError as e:

        print(f"Google Speech Recognition Error: {e}")

        speak(
            "Sorry sir, I cannot connect to the speech recognition service."
        )

        return "none"


    except Exception as e:

        logging.error(f"Recognition Error: {e}")

        print(f"Recognition Error: {e}")

        return "none"


# ============================================================
# 5. WISH ME
# ============================================================

def wish_me():

    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:

        speak("Good morning sir. How are you doing?")

    elif 12 <= hour < 18:

        speak("Good afternoon sir. How are you doing?")

    else:

        speak("Good evening sir. How are you doing?")

    speak(
        "I am JARVIS. Tell me sir, how can I help you?"
    )


# ============================================================
# 6. TIME
# ============================================================

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(
        f"Sir, the current time is {current_time}"
    )


# ============================================================
# 7. DATE
# ============================================================

def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak(
        f"Today is {current_date}"
    )


# ============================================================
# 8. OPEN GOOGLE
# ============================================================

def open_google():

    speak("Okay sir. Opening Google.")

    webbrowser.open(
        "https://www.google.com"
    )


# ============================================================
# 9. OPEN YOUTUBE
# ============================================================

def open_youtube():

    speak("Okay sir. Opening YouTube.")

    webbrowser.open(
        "https://www.youtube.com"
    )


# ============================================================
# 10. OPEN FACEBOOK
# ============================================================

def open_facebook():

    speak("Okay sir. Opening Facebook.")

    webbrowser.open(
        "https://www.facebook.com"
    )


# ============================================================
# 11. OPEN GITHUB
# ============================================================

def open_github():

    speak("Okay sir. Opening GitHub.")

    webbrowser.open(
        "https://github.com"
    )


# ============================================================
# 12. WIKIPEDIA SEARCH
# ============================================================

def search_wikipedia(query):

    try:

        # Remove trigger word
        search_query = query.replace(
            "wikipedia",
            ""
        ).strip()

        if not search_query:

            speak(
                "What should I search on Wikipedia?"
            )

            return


        speak(
            f"Searching Wikipedia for {search_query}"
        )


        results = wikipedia.summary(
            search_query,
            sentences=2
        )


        print("\nWikipedia Result:")
        print(results)


        speak(
            "According to Wikipedia"
        )

        speak(results)


    except wikipedia.exceptions.DisambiguationError:

        speak(
            "There are multiple results. "
            "Please be more specific."
        )


    except wikipedia.exceptions.PageError:

        speak(
            "Sorry sir, I couldn't find that page on Wikipedia."
        )


    except Exception as e:

        logging.error(
            f"Wikipedia Error: {e}"
        )

        print(
            f"Wikipedia Error: {e}"
        )

        speak(
            "Sorry sir, I couldn't search Wikipedia."
        )


# ============================================================
# 13. GOOGLE SEARCH
# ============================================================

def google_search(query):

    search_query = query.replace(
        "search",
        ""
    ).strip()

    if not search_query:

        speak(
            "What would you like me to search?"
        )

        return

    speak(
        f"Searching Google for {search_query}"
    )

    url = (
        "https://www.google.com/search?q="
        + search_query.replace(" ", "+")
    )

    webbrowser.open(url)


# ============================================================
# 14. YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    search_query = query.replace(
        "youtube",
        ""
    ).replace(
        "search",
        ""
    ).strip()

    if not search_query:

        speak(
            "What would you like me to search on YouTube?"
        )

        return

    speak(
        f"Searching YouTube for {search_query}"
    )

    url = (
        "https://www.youtube.com/results?search_query="
        + search_query.replace(" ", "+")
    )

    webbrowser.open(url)


# ============================================================
# 15. MAIN PROGRAM
# ============================================================

def main():

    # Greeting
    wish_me()


    while True:

        # Get voice command
        query = take_command()


        # ----------------------------------------------------
        # Ignore empty commands
        # ----------------------------------------------------

        if query == "none":

            continue


        print(
            f"Command received: {query}"
        )


        # ====================================================
        # TIME
        # ====================================================

        if (
            "time" in query
            or "what time" in query
            or "current time" in query
        ):

            tell_time()


        # ====================================================
        # DATE
        # ====================================================

        elif (
            "date" in query
            or "today's date" in query
            or "today date" in query
        ):

            tell_date()


        # ====================================================
        # NAME
        # ====================================================

        elif (
            "your name" in query
            or "what is your name" in query
            or "who are you" in query
        ):

            speak(
                "My name is JARVIS, sir."
            )


        # ====================================================
        # GOOGLE
        # ====================================================

        elif "open google" in query:

            open_google()


        # ====================================================
        # YOUTUBE
        # ====================================================

        elif "open youtube" in query:

            open_youtube()


        # ====================================================
        # FACEBOOK
        # ====================================================

        elif "open facebook" in query:

            open_facebook()


        # ====================================================
        # GITHUB
        # ====================================================

        elif "open github" in query:

            open_github()


        # ====================================================
        # WIKIPEDIA
        # ====================================================

        elif "wikipedia" in query:

            search_wikipedia(query)


        # ====================================================
        # GOOGLE SEARCH
        # ====================================================

        elif query.startswith("search"):

            google_search(query)


        # ====================================================
        # YOUTUBE SEARCH
        # ====================================================

        elif "search youtube" in query:

            youtube_search(query)


        # ====================================================
        # EXIT
        # ====================================================

        elif (
            "exit" in query
            or "quit" in query
            or "stop" in query
            or "goodbye" in query
            or "shutdown" in query
        ):

            speak(
                "Goodbye sir. Have a nice day."
            )

            break


        # ====================================================
        # HELLO
        # ====================================================

        elif (
            "hello" in query
            or "hi jarvis" in query
            or "hey jarvis" in query
        ):

            speak(
                "Hello sir. How can I help you?"
            )


        # ====================================================
        # THANK YOU
        # ====================================================

        elif (
            "thank you" in query
            or "thanks" in query
        ):

            speak(
                "You're welcome sir."
            )


        # ====================================================
        # UNKNOWN COMMAND
        # ====================================================

        else:

            speak(
                "Sorry sir, I don't know how to do that yet."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nJARVIS stopped by user.")

        try:
            speak("Goodbye sir.")
        except:
            pass

    except Exception as e:

        logging.error(
            f"Application Error: {e}"
        )

        print(
            f"Application Error: {e}"
        )

        speak(
            "Sorry sir, an unexpected error occurred."
        )