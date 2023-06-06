from serial import Serial
import time
arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

while True:
    var= input("input :")
    
    if var=="1":
        ser.write("aim*".encode())
        ser.write(var.encode())
        ser.write("*".encode())
        
    elif var=="2":
        ser.write("num*".encode())
        ser.write(var.encode())
        ser.write("*".encode())
        
    elif var=="3":
        ser.write("num*".encode())
        ser.write(var.encode())
        ser.write("*".encode())
    
    ser.write("score*".encode())
    # time.sleep(1)
    ser.write(var.encode())
    ser.write("*".encode())
    
    # command = ser.readline().decode().strip()
    # print(command)
    time.sleep(1.)
    # for i in range(6):
    #     ser.write(var.encode())
    #     time.sleep(1.)
        # if ser.in_waiting > 0:
        
ser.close


