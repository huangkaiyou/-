from gpiozero import MCP3008
import time
vref=3.3
# while True:
#     vol= MCP3008(channel= 0, select_pin=8) #choose channel from 0 to 7, cs for specifit device
#     vol= vol*vref
#     time.sleep(.5)

voltage=[]
for i in range(6):
    vol= MCP3008(channel= i, select_pin=8)
    voltage.append(vol.value)
while True:
    #judgement for hitting board
    threshold= 2 #lower represent has hit
    # a~f is No.1~6 for brush
    a= voltage[0]<threshold
    b= voltage[1]<threshold
    c= voltage[2]<threshold
    d= voltage[3]<threshold
    e= voltage[4]<threshold
    f= voltage[5]<threshold

    number_board= ['num1','num2','num3','num4','num5','num6''num7','num8','num9',]
    if a == True:
        if d== True:
            hit= number_board[0]
        elif e== True:
            hit= number_board[3]
        elif f== True:
            hit= number_board[6]
    elif b == True:
        if d== True:
            hit= number_board[1]
        elif e== True:
            hit= number_board[4]
        elif f== True:
            hit= number_board[7]
    elif c == True:
        if d== True:
            hit= number_board[2]
        elif e== True:
            hit= number_board[5]
        elif f== True:
            hit= number_board[8]
    print(hit)
gpio.cleanup()