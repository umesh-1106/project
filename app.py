import base64
import numpy as np
import cv2
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    # 1. Grab the json payload sent from the browser
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'error': 'No image data received'}), 400

    # 2. Extract and decode the base64 string
    header, encoded = data['image'].split(",", 1)
    decoded_bytes = base64.b64decode(encoded)
    
    # 3. Convert bytes into an OpenCV image array
    nparr = np.frombuffer(decoded_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is None:
        return jsonify({'error': 'Failed to decode image'}), 400

    # -----------------------------------------------------------------
    # INSERT YOUR DETECTION CODE HERE
    # Run your vehicle and parking zone algorithms directly on 'frame'
    # Example: frame = your_detection_model.detect(frame)
    # -----------------------------------------------------------------
    
    # 4. Re-encode the newly drawn frame back into a JPEG buffer
    _, buffer = cv2.imencode('.jpg', frame)
    processed_base64 = base64.b64encode(buffer).decode('utf-8')
    
    # 5. Return the string right back to the browser
    return jsonify({
        'processed_image': f"data:image/jpeg;base64,{processed_base64}"
    })

if __name__ == '__main__':
    app.run()
