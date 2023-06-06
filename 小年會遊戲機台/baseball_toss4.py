import time
from serial import Serial
import random
from playsound import playsound
# playsound("C:/Users/user/Downloads/s.mp3")

arduino_port = "COM5"  # Replace with your Arduino's port
ser0 = Serial("COM5", baudrate= 9600, timeout=0.1) #input data
ser1 = Serial("COM3", baudrate= 9600, timeout=0.1) #output data


    
while True:
    # if ser.in_waiting > 0:
    hit=0
    count= 0   # current used ball
    balls= 10   # the total ball number
    score= 0
    hit_condition= 0 
    
    wait1= 3 #prepare for next ball
    wait2= 5 #prepare for next round

    # timing block
    timing= 8   #the interval of time
    time_count= 0 #timing for display

    #bingo block
    number_all = []    #  用於儲存賓果盤
    line = []        #  用於儲存每條線尚未中獎的數字個數
    #  將數字1～9放進number_all
    for i in range(1,10):
        number_all.append(i)

    #  將每條線尚未中獎的數字個數預設為3
    for k in range(8):
        line.append(3)

        #the start botton 
        # command = ser.readline().decode().strip()
        # if command == "s": 
        #     print('start!')
    
    
    ser1.write("game_con".encode())
    ser1.write("*".encode())
    ser1.write("initial".encode()) #enable the brush
    ser1.write("*".encode()) 
    # a= input("input : ") #start messenge from arduino (button)
    # if a=="0":
    command_start = ser0.readline().decode().strip() 
    # while (command_start!="start"):
    #     pass
    # command_start= 0
    if command_start== "start":
        
        # brush block
        
        time.sleep(1)
        ser1.write("game_con".encode())
        ser1.write("*".encode())
        ser1.write("ready".encode()) #enable the brush
        ser1.write("*".encode())
        print('ready ?') #on arduino, lcd will display ready screeen        
        time.sleep(2)
        print('GO !')
        
        playsound("C:/Users/user/Downloads/s.mp3") #sound for START
        
        ser1.write("game_con".encode())
        ser1.write("*".encode())
        ser1.write("main".encode()) #enable the brush
        ser1.write("*".encode())
        aim= random.choice(number_all)
        print("aim",aim) #the target
        
        ser0.write("brush_con".encode())
        ser0.write("*".encode())
        ser0.write("enable".encode()) #enable the brush
        ser0.write("*".encode())
        
        time0 = time.perf_counter()   # begining 
        time1 = time0   # current time
        
        aim= random.choice(number_all)
        while (aim in number_all)==0:
                aim= random.choice(number_all)
        ser1.write("aim_con".encode())
        ser1.write("*".encode())
        ser1.write(str(aim).encode())
        ser1.write("*".encode()) 
        print("aim",aim) #the target
        
        ser1.write("ball_con*".encode())
        leftball= balls- count
        ser1.write(str(leftball).encode())
        ser1.write("*".encode())
        print("left ball : ", balls- count) 
        
        while (count<= balls): 
            #next ball start ! 
            
            
            command = ser0.readline().decode().strip() 
            if command in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                hit= int(command)
            
            #use a ball
            if (hit!= 0 or  (time1-time0)>=timing):
                                 
                ser0.write("brush_con".encode())
                ser0.write("*".encode())
                ser0.write("disable".encode()) #stop the brush
                ser0.write("*".encode())
                print('the number you hit : ', hit) 
                hit_condition= True 
                count= count+1 
                
                aim= random.choice(number_all)
                while (aim in number_all)==0:
                    aim= random.choice(number_all)
                ser1.write("aim_con".encode())
                ser1.write("*".encode())
                ser1.write(str(aim).encode())
                ser1.write("*".encode()) 
                print("aim",aim) #the target
                
                ser1.write("ball_con*".encode())
                leftball= balls- count
                ser1.write(str(leftball).encode())
                ser1.write("*".encode())
                print("left ball : ", balls- count) 
                
                #block for hitting 
                
                #judge whether has hit                
                if (hit in number_all):
                    score+=10    
                    
                    #bingo
                    #  若中獎號碼在某直排
                    for check_column in range(3):
                        if(number_all.index((hit)) % 3 == check_column):
                                line[check_column] -= 1
                    #  若中獎號碼在某橫排
                    for check_row in range(3):
                        if(number_all.index((hit)) // 3 == check_row):
                                line[check_row+3] -= 1
                    #  若中獎號碼在斜排
                    if(number_all.index((hit)) == 0):
                        line[6] -= 1
                    elif(number_all.index((hit)) == 8):
                        line[6] -= 1
                    elif(number_all.index((hit)) == 4):
                        line[6] -= 1
                        line[7] -= 1
                    elif(number_all.index(int(hit)) % 2 == 0 ):
                        line[7] -= 1
                    
                    #  判斷連線幾條
                    for i in line:
                        if i==0:
                            # line.remove(i)
                            balls+=1 #effect of bingo
                    count_bingo=0
                    
                    #left number list
                    number_all.remove(hit) #remove from number list
                    
                    #calculate the score
                    
                    if hit==aim:
                        score+=20
                        
                    #transmit the result to arduino
                    ser1.write("score_con*".encode())
                    ser1.write(str(score).encode())
                    ser1.write("*".encode())
                    print("score : ", score) 
                    
                    ser1.write("hit_con*".encode())
                    ser1.write(str(hit).encode())
                    ser1.write("*".encode())
                    
                    #info that need to change after hitting a board
                if (hit !=0 ):
                    playsound("C:/Users/user/Downloads/MLG Horns - MLG Sound Effects (HD).mp3")                     

                # if (count<=balls-1):
                    time.sleep(wait1)
                    playsound("C:/Users/user/Downloads/HOLY SHIT! Unreal Tournament Sound.mp3") #sound for next ball
                    ser0.write("brush_con".encode())
                    ser0.write("*".encode())
                    ser0.write("enable".encode())
                    ser0.write("*".encode())
                    
                    #prepare for next ball
                    # print("Next ball")
                
                if ((time1-time0)>timing):
                    time_count=0
                    ser1.write("time_con*".encode())
                    ser1.write(str("0").encode())
                    ser1.write("*".encode())
                    playsound("C:/Users/user/Downloads/s.mp3") #sound for over time 
                time0 = time.perf_counter()   # begining 
                time1 = time0   # current time
                time_count=0
                hit=0
                    
            #print the left time
            if (time1-time0)>=time_count:
                ser1.write("time_con*".encode())
                lefttime= timing-int(time1-time0)
                ser1.write(str(lefttime).encode())
                ser1.write("*".encode())
                print(lefttime)
                time_count+=2
                
            time1 = time.perf_counter()   # renew the current time
                
                
                    
        ser1.write("game_con*".encode())
        ser1.write("end".encode())
        ser1.write("*".encode())
        print("game over")
        time.sleep(wait2)
        
        ser1.write("game_con".encode())
        ser1.write("*".encode())
        ser1.write("initial".encode()) #enable the brush
        ser1.write("*".encode())
        print("play game !!!")
            
        # command = ser.readline().decode().strip() #search for start command
        a= input("input : ") 