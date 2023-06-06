from serial import Serial
import time
arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

while True:
    var= input("input :")
    ser.write(var.encode())
    ser.write("*".encode())
    time.sleep(.1)

    command = ser.readline().decode().strip()
    print(command)
    
ser.close


