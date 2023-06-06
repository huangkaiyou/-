from playsound import playsound
playsound("C:/Users/user/Downloads/s.mp3")

from serial import Serial
import time
arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

while True:
    # Serial.send('a')
    if ser.in_waiting > 0:
        command = ser.readline().decode().strip()
        if command == "s":
            print('play')
            playsound("C:/Users/user/Downloads/MLG Horns - MLG Sound Effects (HD).mp3")
            time.sleep(1)
            
        