import random    #  載入隨機函數
number_all = []    #  用於儲存賓果盤
line = []        #  用於儲存每條線尚未中獎的數字個數
count_bingo=0    # 數目前幾條bingo
#  將數字1～9放進number_all
for i in range(1,10):
    number_all.append(i)

#  將每條線尚未中獎的數字個數預設為3
for k in range(8):
    line.append(3)
    
while(True):  #  當尚未連線則執行
    #    由使用者輸入中獎號碼
    hit = input("中獎號碼：")
    print()        #換行
    #  若中獎號碼在某直排
    for check_column in range(3):
        if(number_all.index(int(hit)) % 3 == check_column):
                line[check_column] -= 1
    #  若中獎號碼在某橫排
    for check_row in range(3):
        if(number_all.index(int(hit)) // 3 == check_row):
                line[check_row+3] -= 1
    #  若中獎號碼在斜排
    if(number_all.index(int(hit)) == 0):
        line[6] -= 1
    elif(number_all.index(int(hit)) == 8):
        line[6] -= 1
    elif(number_all.index(int(hit)) == 4):
        line[6] -= 1
        line[7] -= 1
    elif(number_all.index(int(hit)) % 2 == 0 ):
        line[7] -= 1
    
    #  判斷連線幾條
    for i in range(8):
        if line[i]==0:
            count_bingo+=1
    print(count_bingo)
    count_bingo=0
    