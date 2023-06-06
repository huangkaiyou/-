import time
import ramdom
from serial import Serial

arduino_port = "COM5"  # Replace with your Arduino's port
ser = Serial(arduino_port, 9600)

wait1= 5 #prepare for next ball
wait2= 5 #prepare for next round

# timing block
timing= 3   #time for each ball

number_board= ["num1","num2","num3","num4","num5","num6","num7","num8","num9"] 

# String hit 
# hit = "not hit" 



            
while True:
    # if ser.in_waiting > 0:
    
    count= 0   # current used ball
    balls= 10   # the total ball number
    
    hit_condition= 0 
    #the start botton 
    command = ser.readline().decode().strip()
    if command == "s": 
        print('start!')
        # brush block
            
        time.sleep(3)
        print('ready ?')
        time.sleep(1)
        print('GO !')   
         
        time0 = time.perf_counter()   # begining 
        time1 = time0   # current time
        
        while (count<= balls): 
            command = ser.readline().decode().strip() 
            if command in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                hit= int(command)
                
                if (hit!= 0 or  (time1-time0)>timing):
                    print('the number you hit : ', hit) 
                    hit_condition= True 
                    count= count+1 
                    
                    if (count<=balls-1):
                        print("left ball : ", balls- count) 
                        time.sleep(wait1) 
                        time0 = time.perf_counter()   # begining 
                        time1 = time0   # current time
                        print("Next ball") 
                    
                time1 = time.perf_counter()   # renew the current time
            
        print("game over") 
        time.sleep(wait2)
        print("play game !!!")
    command = ser.readline().decode().strip()
        
