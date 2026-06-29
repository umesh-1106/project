from flask import Flask, render_template, Response, redirect, url_for
import cv2

app = Flask(__name__)

# -------------------------------
# Camera
# -------------------------------
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()

        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame +
               b'\r\n')


# -------------------------------
# Routes
# -------------------------------

@app.route('/')
def home():
    return redirect(url_for('dashboard'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():

    return render_template(
        'dashboard.html',
        vehicle_count=0,
        wrong_count=0,
        today_count=0,
        detected_vehicle="Waiting...",
        owner_name="--",
        parking_status="Waiting",
        location="--",
        detected_time="--",
        records=[]
    )


@app.route('/camera')
def camera_page():

    return render_template(
        'camera.html',
        detected_vehicle="Waiting...",
        owner_name="--",
        vehicle_type="--",
        parking_zone="--",
        parking_status="Waiting",
        detected_time="--"
    )


@app.route('/register')
def register():

    return render_template("register.html")


@app.route('/history')
def history():

    return render_template(
        "history.html",
        history=[]
    )


@app.route('/video_feed')
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
