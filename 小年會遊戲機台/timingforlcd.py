import time
from serial import Serial
import ramdom
arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

time.sleep(5)
timing= 10   #the interval of time
time0 = time.perf_counter()  # begining 
time1 = time0   # current time
time_count= 0 #timing for display

while True:
  while time_count<=timing:
    if (time1-time0)>time_count:
      ser.write("time*".encode())
      # time.sleep(1)
      # ser.write("left time : ".encode())
      tim_value= timing-int(time1-time0)
      ser.write(str(tim_value).encode())
      ser.write("*".encode())
      print(timing-int(time1-time0))
      time_count+=2
      time1 = time.perf_counter()

    time1 = time.perf_counter()   # renew the current time
  time.sleep(5)
  timing= 10   #the interval of time
  time0 = time.perf_counter()  # begining 
  time1 = time0   # current time
  time_count= 0 #timing for display

