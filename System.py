from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image 
import sqlite3
from PyQt5.QtCore import  QDateTime
import qrcode
import random
import string


def Preprocess(qimage):
    # Convert QImage to Pillow Image
    image = Image.fromqpixmap(qimage)

    # Convert the image to grayscale if necessary
    image = image.convert('L')

    # Convert the Pillow Image to NumPy array
    image_array = np.array(image)
    
    return image_array


def Get_Code(Image):
    QR_info = decode(Image)
    
    # Check if any QR codes were detected
    if QR_info:
        # Extract data from the first QR code object
        data = QR_info[0].data
        Code = data.decode()
        return Code
    else:
        return None  # No QR code detected in the image


def Check_Access(Code):
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    query = 'SELECT * FROM Users WHERE Code = ?'
    cur.execute(query, (Code,))
    result = cur.fetchone()
    # Close Database Connection :
    conn.close()
    return result

def Registre(Result):
    # Get the current date and time as formatted_datetime
    current_datetime = QDateTime.currentDateTime()
    formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")

    # Connect to the SQLite database
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    # Split the formatted_datetime into date and time
    date, time = formatted_datetime.split(' ')

    # Insert data into the Historique table
    cur.execute("INSERT INTO Historique (Name, Code,Date,Time) VALUES (?, ?, ?, ?)",
                (Result[1], Result[2], date, time))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
    
def generate_random_data(length):
    characters = string.ascii_letters + string.digits
    random_data = ''.join(random.choice(characters) for _ in range(length))
    return random_data

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    # Convert To Image using Pilow
    img_pil = qr.make_image(fill_color="black", back_color="white")
    return img_pil

def Add_New_User(Name,Code):
    # Connect to the SQLite database
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    # Insert data into the Historique table
    cur.execute("INSERT INTO Users (Name, Code) VALUES (?, ?)",
                (Name,Code))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()































