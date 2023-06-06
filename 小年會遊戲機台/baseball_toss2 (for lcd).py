import time
from serial import Serial
while True:
    
    # brush block
    wait= 50/1000 #avoid instant unstable signal
    wait1= 3 #prepare for next ball

    threshold= 1#  #lower represent has hit
    brush= [2,4,7,8,12,13]
    count= 0   # current used ball
    balls= 10   # the total ball number
    number_board= ["num1","num2","num3","num4","num5","num6","num7","num8","num9"] 
    
     # String hit 
     # hit = "not hit" 
    hit= 0 
    hit_condition= 0 
    
     # timing block
    timing= 3   #the interval of time
    time0 = time.perf_counter()  # begining 
    time1 = time0   # current time
    time_count= 0 #timing for display

     #  # score rule block
     # char *bingo_list[][]= {{"num1", "num2", "num3"}, {"num4", "num5", "num6"}, {"num7", "num8", "num9"}, {"num1", "num4", "num7"}, {"num2", "num5", "num8"}, {"num3", "num6", "num9"}, {"num1", "num5", "num9"}, {"num3", "num5", "num7"}} 
     # char *bingo[]= {} 
    
    while (count<= balls):   
        if (hit!= 0 or  (time1-time0)>timing):
            # Serial.println(hit) 
            hit_condition= True 
            count= count+1 
            
            if (count<=balls-1):
                # Serial.print("left ball : ") 
                # Serial.println(balls- count) 
                time.sleep(wait1) 
                print('yes')
                time0 = time.perf_counter() # begining 
                time1 = time0   # current time
                time_count=0
                # Serial.println("Next ball") 
            
        time1 = time.perf_counter()   # renew the current time
        if (time1-time0)>time_count:
            print("left time : ", timing-int(time1-time0))
            time_count+=1
        
    Serial.println("game over") 
    time.sleep(5000) 
