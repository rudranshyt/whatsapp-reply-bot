import pywhatkit
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    phone_number = request.form["phoneNumber"]
    encoded_message = request.form["message"]
    decoded_message = unquote(encoded_message)
    number_of_times = int(request.form["numberOfTimes"])

    for _ in range(number_of_times):
        pywhatkit.sendwhatmsg_instantly(phone_number, decoded_message)

    return "Messages sent successfully!"


if __name__ == "__main__":
    app.run(debug=True)
