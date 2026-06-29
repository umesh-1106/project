import cv2

class VideoCamera:

    def __init__(self):

        # Open Webcam
        self.camera = cv2.VideoCapture(0)

        # Set Camera Resolution
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def __del__(self):

        self.camera.release()

    def get_frame(self):

        success, frame = self.camera.read()

        if not success:
            return None

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)

        return buffer.tobytes()


camera = VideoCamera()


def generate_frames():

    while True:

        frame = camera.get_frame()

        if frame is None:
            break

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )
