import pywhatkit
from flask import Flask, request, render_template
from urllib.parse import unquote
import schedule
import threading
import time

app = Flask(__name__)

scheduled_messages = {}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    phone_number = request.form["phoneNumber"]
    encoded_message = request.form["message"]
    decoded_message = unquote(encoded_message)
    number_of_times = int(request.form["numberOfTimes"])
    
    send_instant_messages(phone_number, decoded_message, number_of_times)
    
    # If scheduled time is provided, schedule the message
    scheduled_time = request.form.get("scheduledTime")
    if scheduled_time:
        schedule_message(phone_number, decoded_message, scheduled_time)

    return "Messages sent successfully!"

def send_instant_messages(phone_number, message, number_of_times):
    for _ in range(number_of_times):
        pywhatkit.sendwhatmsg_instantly(phone_number, message)

def send_scheduled_message(phone_number, message):
    pywhatkit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)

def schedule_message(phone_number, message, scheduled_time):
    scheduled_messages[scheduled_time] = (phone_number, message)
    scheduled_time_parts = scheduled_time.split(":")
    hour = int(scheduled_time_parts[0])
    minute = int(scheduled_time_parts[1])
    schedule.every().day.at(scheduled_time).do(send_scheduled_message, phone_number, message)

def scheduled_message_sender():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    
    sender_thread = threading.Thread(target=scheduled_message_sender)
    sender_thread.start()

    app.run(debug=True)
