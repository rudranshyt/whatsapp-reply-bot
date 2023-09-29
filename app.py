import pywhatkit
from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    phone_number = request.form["phoneNumber"]
    message = request.form["message"]
    number_of_times = int(request.form["numberOfTimes"])
    
    send_messages(phone_number, message, number_of_times)
    
    
    scheduled_time = request.form.get("scheduledTime")
    if scheduled_time:
        schedule_message(phone_number, message, scheduled_time)

    return "Messages sent successfully!"

def send_messages(phone_number, message, number_of_times):
    for _ in range(number_of_times):
        pywhatkit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)

def schedule_message(phone_number, message, scheduled_time):
    scheduled_time_parts = scheduled_time.split(":")
    hour = int(scheduled_time_parts[0])
    minute = int(scheduled_time_parts[1])
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

if __name__ == "__main__":
    app.run(debug=True)
