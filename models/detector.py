from ultralytics import YOLO
import cv2

class NumberPlateDetector:

    def __init__(self):

        # Load YOLOv8 model
        self.model = YOLO("yolov8/best.pt")

    def detect(self, frame):

        results = self.model(frame)

        plates = []

        for result in results:

            boxes = result.boxes

            for box in boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                if confidence > 0.5:

                    plate = frame[y1:y2, x1:x2]

                    plates.append({
                        "image": plate,
                        "bbox": (x1, y1, x2, y2),
                        "confidence": confidence
                    })

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0,255,0),
                        2
                    )

                    cv2.putText(
                        frame,
                        f"Plate {confidence:.2f}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2
                    )

        return frame, plates


detector = NumberPlateDetector()
