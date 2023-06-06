from serial import Serial
import time
arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

while True:
    var= input("input :")
    ser.write("score*".encode())
    # ser.write('*'.encode())
    
    time.sleep(.1)
    # ser.write('\n'.encode())
    # ser.write(var.encode())
    # ser.write('\n'.encode())
    
    # time.sleep(0.6)
    command = ser.readline().decode().strip()
    print(command)
    # ser.write("b".encode())
    # ser.write("c".encode())
    
    
    # ser.write(var.encode())
    # for i in range(6):
    #     time.sleep(1.)
    #     ser.write(var.encode())
        
    #     # if ser.in_waiting > 0:
    #     command = ser.readline().decode().strip()
    #     print(command)
ser.close


