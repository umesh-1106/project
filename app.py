from flask import Flask, render_template, request
import sqlite3
import os
import easyocr
from twilio.rest import Client

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reader = easyocr.Reader(['en'])

# Twilio Configuration
ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_NUMBER = "+1234567890"

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def get_phone(vehicle):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT phone FROM vehicles WHERE number=?", (vehicle,))
    data = cur.fetchone()

    conn.close()

    if data:
        return data[0]
    return None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    result = reader.readtext(path)

    vehicle = ""

    for r in result:
        vehicle += r[1]

    vehicle = vehicle.replace(" ", "")

    phone = get_phone(vehicle)

    if phone:

        client.messages.create(
            body=f"Warning! Your vehicle {vehicle} is wrongly parked.",
            from_=TWILIO_NUMBER,
            to=phone
        )

        return f"Message Sent Successfully to {vehicle}"

    else:
        return "Vehicle Number Not Found"


if __name__ == "__main__":
    app.run(debug=True)
