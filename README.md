# Flask Keylogger Web App

# 🖥️ Flask Keylogger Web App

A simple Flask web application that controls a basic keylogger. It captures keyboard input, clipboard content, system information, a screenshot, and a short audio recording. All data is saved locally and viewable/downloadable via a web interface.


## 🚀 Features

- ✅ Start/Stop the keylogger from the browser
- 🖱️ Capture system and clipboard data
- 📷 Take a screenshot
- 🎙️ Record a short audio clip (5 seconds)
- 📄 View captured keystrokes in the browser
- ⬇️ Download logs, audio, and image files


## 🧰 Technologies Used

- **Python 3**
- **Flask** – web framework
- **Pynput** – for keyboard input
- **Pillow** – for screenshots
- **sounddevice & scipy** – for audio recording
- **win32clipboard** – for clipboard access
- **Cryptography** (optional)
- **HTML** – for basic frontend


## 📁 Project Structure

flask-keylogger/
├── app.py # Main Flask application
├── keylogger.py # Keylogging logic and data capture
├── templates/
│ └── index.html # Web interface
├── static/ # (Optional) Store screenshots/audio for access
└── README.md


## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/flask-keylogger.git
cd flask-keylogger

2.**Create and activate a virtual environment (optional but recommended):**

python -m venv venv
venv\Scripts\activate  # On Windows

3.**Install dependencies:**

pip install -r requirements.txt

▶️ Running the App

python app.py

Then open your browser and go to:
http://127.0.0.1:5000/

📄 Logs and Files Saved

By default, files are saved to:

C:\Users\<YourName>\Documents\KeyLogger\

Saved files:

    key_log.txt — captured keystrokes

    syseminfo.txt — system details

    clipboard.txt — clipboard content

    screenshot.png — screenshot image

    audio.wav — microphone recording

## 📸 Screenshot

![Web page Screenshot](https://github.com/sathya-selvz/Flask-Keylogger-Web-App/blob/main/screenshots/Screenshot1.png?raw=true?raw=true)



