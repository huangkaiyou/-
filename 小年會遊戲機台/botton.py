import time
from serial import Serial

arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

while True:
    if ser.in_waiting > 0:
        command = ser.readline().decode().strip()
        if command in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print('play')
            time.sleep(1)