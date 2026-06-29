import mysql.connector
from config import Config

# -----------------------------
# Database Connection
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

# -----------------------------
# Register Vehicle
# -----------------------------
def register_vehicle(vehicle_number,
                     owner_name,
                     phone,
                     vehicle_type,
                     vehicle_color,
                     parking_zone,
                     address):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO vehicles
    (vehicle_number,
     owner_name,
     phone,
     vehicle_type,
     vehicle_color,
     parking_zone,
     address)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        vehicle_number,
        owner_name,
        phone,
        vehicle_type,
        vehicle_color,
        parking_zone,
        address
    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()

# -----------------------------
# Find Vehicle
# -----------------------------
def get_vehicle(vehicle_number):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM vehicles WHERE vehicle_number=%s",
        (vehicle_number,)
    )

    vehicle = cursor.fetchone()

    cursor.close()
    conn.close()

    return vehicle

# -----------------------------
# Save Wrong Parking
# -----------------------------
def save_wrong_parking(vehicle,
                       location,
                       image_path):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO wrong_parking
    (vehicle_number,
     owner_name,
     vehicle_type,
     parking_zone,
     location,
     image_path)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        vehicle["vehicle_number"],
        vehicle["owner_name"],
        vehicle["vehicle_type"],
        vehicle["parking_zone"],
        location,
        image_path
    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()

# -----------------------------
# History
# -----------------------------
def get_history():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM wrong_parking
        ORDER BY detected_time DESC
    """)

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history

# -----------------------------
# Dashboard Counts
# -----------------------------
def total_vehicles():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM vehicles")

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count


def total_wrong_parking():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM wrong_parking")

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count
