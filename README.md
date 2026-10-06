# 🤖 JARVIS – Voice Assistant

A **Python-based voice assistant** inspired by JARVIS that allows users to interact with their computer using **voice commands**.

JARVIS can listen to spoken commands, convert speech to text, perform web searches, retrieve information from Wikipedia, open popular websites, provide the current time/date, and respond using **Windows text-to-speech**.

---

## ✨ Features

- 🎙️ **Voice Input**
  - Captures commands through the microphone.
  - Converts speech to text using Google Speech Recognition.
  - Supports English (India) using `en-IN`.

- 🔊 **Voice Output**
  - Uses `pyttsx3` with Windows **SAPI5**.
  - Provides spoken responses for commands.
  - Creates a fresh TTS engine for each response to improve reliability.

- 🧠 **Wikipedia Search**
  - Search Wikipedia using voice commands.
  - Reads the first two sentences of the result.

- 🔎 **Google Search**
  - Opens Google search results based on your voice command.

- ▶️ **YouTube Search**
  - Searches YouTube directly from voice commands.

- 🌐 **Website Automation**
  - Open:
    - Google
    - YouTube
    - Facebook
    - GitHub

- 🕐 **Time & Date**
  - Tells the current time.
  - Provides the current date.

- 👋 **Greeting System**
  - Automatically responds with:
    - Good morning
    - Good afternoon
    - Good evening

- 💬 **Basic Conversation**
  - Responds to:
    - Hello / Hi JARVIS
    - Thank you / Thanks
    - What is your name?
    - Who are you?

- 🛑 **Exit Commands**
  - Supports commands such as:
    - `exit`
    - `quit`
    - `stop`
    - `goodbye`
    - `shutdown`

- 📝 **Logging**
  - Application errors and important events are stored in:
    `logs/application.log`

---

## 🏗️ Project Architecture

```text
User
  │
  │ Voice Command
  ▼
┌───────────────────────┐
│   Microphone Input    │
│  SpeechRecognition    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Command Processing  │
│     Python Logic      │
└───────────┬───────────┘
            │
      ┌─────┴─────────┐
      │               │
      ▼               ▼
  Local Commands   Web Services
      │               │
      ├── Time        ├── Google
      ├── Date        ├── YouTube
      ├── Websites    └── Wikipedia
      └── Greetings
            │
            ▼
┌───────────────────────┐
│    Text-to-Speech     │
│       pyttsx3         │
│       Windows SAPI5   │
└───────────┬───────────┘
            │
            ▼
       🔊 JARVIS Voice
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech-to-text |
| Google Speech Recognition | Voice recognition |
| pyttsx3 | Text-to-speech |
| Windows SAPI5 | Voice output |
| Wikipedia API | Wikipedia information |
| webbrowser | Opening websites/searches |
| datetime | Time and date |
| logging | Application logging |

The implementation uses `speech_recognition`, `pyttsx3`, `wikipedia`, `webbrowser`, `datetime`, and Python logging.

---

## 📁 Project Structure

```text
Jarvis/
│
├── jarvis.py
│
├── logs/
│   └── application.log
│
├── requirements.txt
│
└── README.md
```

> Rename your main Python file to `jarvis.py` if it currently has a different name.

---

## ⚙️ Requirements

### Software

- Windows 10/11
- Python 3.9+
- Working microphone
- Internet connection

### Python Libraries

```txt
SpeechRecognition
pyttsx3
wikipedia
PyAudio
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/jarvis.git
```

```bash
cd jarvis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows CMD:**

```bash
venv\Scripts\activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `PyAudio` gives an installation error on Windows, install an appropriate Windows-compatible PyAudio package/version for your Python environment.

### 4. Run JARVIS

```bash
python jarvis.py
```

---

## 🎙️ Example Voice Commands

### Basic Commands

```text
Hello Jarvis
Hi Jarvis
What is your name?
Who are you?
Thank you
```

### Time & Date

```text
What is the time?
What is the current time?
What is today's date?
```

### Websites

```text
Open Google
Open YouTube
Open Facebook
Open GitHub
```

### Google Search

```text
Search Python programming
Search artificial intelligence
Search latest technology
```

### YouTube Search

```text
Search YouTube Python tutorial
Search YouTube machine learning
```

### Wikipedia

```text
Wikipedia Virat Kohli
Wikipedia Artificial Intelligence
Wikipedia Python
```

### Exit

```text
Exit
Quit
Stop
Goodbye
Shutdown
```

---

## 🔄 How It Works

### 1. Microphone Input

JARVIS listens to the microphone using `SpeechRecognition`.

The recognizer is configured with:

```python
recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
```

These settings help JARVIS handle pauses and changing background noise.

### 2. Speech Recognition

The recorded audio is converted into text using Google's speech recognition service:

```python
query = recognizer.recognize_google(
    audio,
    language="en-IN"
)
```



### 3. Command Processing

The recognized command is converted to lowercase and checked against supported commands.

For example:

```python
if "open google" in query:
    open_google()
```

The main loop handles commands such as time, date, websites, Wikipedia, searches, greetings, and exit commands.

### 4. Text-to-Speech

JARVIS converts its response back into speech using Windows SAPI5:

```python
engine = pyttsx3.init("sapi5")
engine.say(str(text))
engine.runAndWait()
```



---

## 📝 Logging

JARVIS automatically creates a `logs` directory and stores application logs in:

```text
logs/application.log
```

The logging system is initialized with Python's built-in `logging` module.

This helps identify errors related to:

- Microphone
- Speech recognition
- Text-to-speech
- Wikipedia
- Application execution

---

## 🛡️ Error Handling

The application handles several common errors.

### Speech Recognition

If JARVIS cannot understand the command:

```text
Sorry sir, I didn't understand.
```

### Internet / Recognition Service

If Google Speech Recognition cannot be reached:

```text
Sorry sir, I cannot connect to the speech recognition service.
```

### Wikipedia

JARVIS handles:

- Disambiguation errors
- Page not found errors
- Other Wikipedia errors

### Application Errors

Unexpected errors are logged and JARVIS provides a voice response instead of immediately crashing.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Build a practical voice-controlled assistant using Python.
2. Implement speech-to-text functionality.
3. Implement text-to-speech functionality.
4. Automate common web activities using voice commands.
5. Integrate external information sources such as Wikipedia.
6. Implement error handling and application logging.
7. Create a foundation for a more advanced AI assistant.

---

## 🚧 Current Limitations

The current version primarily supports predefined commands.

It does **not yet provide**:

- Large Language Model integration
- General conversational AI
- Wake-word detection
- Continuous background listening
- System-level application control
- Email automation
- Weather integration
- Calendar integration
- Smart home control
- Agentic AI / tool-calling
- Long-term memory

These can be added in future versions.

---

## 🔮 Future Enhancements

### Phase 1 – More Automation

- Open desktop applications
- Control volume
- Control system settings
- Take screenshots
- File management
- Application launching

### Phase 2 – AI Integration

Integrate an LLM to support natural conversations:

```text
User
 ↓
Voice Input
 ↓
Speech-to-Text
 ↓
LLM
 ↓
Tool / Function Calling
 ↓
Response
 ↓
Text-to-Speech
```

### Phase 3 – Advanced JARVIS

Potential features:

- 🤖 OpenAI / Gemini integration
- 🧠 Long-term memory
- 🔍 Web research
- 📧 Email automation
- 📅 Calendar management
- 📂 File search
- 🖥️ Computer control
- 🔗 API integrations
- 🧩 Tool calling
- 🔄 Agentic workflows
- 🎤 Wake-word detection

---

## 💡 Learning Outcomes

Through this project, you can demonstrate experience with:

- Python
- Object/function-based programming
- Speech recognition
- Text-to-speech
- API/service integration
- Web automation
- Exception handling
- Logging
- Environment setup
- Voice-based human-computer interaction

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new JARVIS feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

## 📄 License

This project is intended for educational and personal development purposes.

You can add an MIT License if you want to make the project open source under the MIT terms.

---

## 👨‍💻 Author

**M.Sriram Sai Eswar**

Computer Science & Engineering | AI & ML

Interested in:

- Artificial Intelligence
- Machine Learning
- Generative AI
- Agentic AI
- Python Development
- AI Engineering

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

### 🚀 JARVIS

> **"Goodbye sir. Have a nice day."**
