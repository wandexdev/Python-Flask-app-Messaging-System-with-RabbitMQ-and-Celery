from flask import Flask, request, jsonify
import logging
from datetime import datetime
from tasks import send_email_task
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set up logging
log_file = '/var/log/messaging_system.log'
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.INFO)

@app.route('/', methods=['GET'])
def message_handler():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email_task(sendmail)
        return f"Email task to {sendmail} has been queued.", 200

    if talktome is not None:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f'Current time logged: {current_time}')
        return f"Current time {current_time} has been logged.", 200

    return {
        "error": "Please provide a valid parameter.",
        "valid_parameters": ["sendmail", "talktome"]
    }, 400

@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open(log_file, 'r') as file:
            logs = file.read()
        return "<pre>" + logs + "</pre>", 200
    except Exception as e:
        return {
            "error": "Could not read log file.",
            "message": str(e)
        }, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

