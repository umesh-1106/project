import os

class Config:

    # Flask Secret Key
    SECRET_KEY = "wrong_parking_project_2026"

    # Upload Folder
    UPLOAD_FOLDER = "static/uploads"

    # Allowed Image Extensions
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

    # Camera ID
    CAMERA_ID = 0

    # ----------------------------
    # MySQL Configuration
    # ----------------------------

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "wrong_parking_db"

    # ----------------------------
    # YOLO Model
    # ----------------------------

    YOLO_MODEL = "yolov8/best.pt"

    # ----------------------------
    # EasyOCR
    # ----------------------------

    OCR_LANGUAGES = ['en']

    # ----------------------------
    # Camera Resolution
    # ----------------------------

    FRAME_WIDTH = 1280
    FRAME_HEIGHT = 720

    # ----------------------------
    # Parking Zone
    # ----------------------------

    PARKING_ZONE = "College Parking"

    # ----------------------------
    # Debug Mode
    # ----------------------------

    DEBUG = True
