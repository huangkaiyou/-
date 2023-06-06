import random    #  載入隨機函數
number_all = []    #  用於儲存賓果盤
line = []        #  用於儲存每條線尚未中獎的數字個數
Bingo = 1        #  用於判斷是否連線的變數
#  將數字1～9放進number_all
for i in range(1,10):
    number_all.append(i)

#  印出賓果盤，每3個數字換行
for j in range(9):
    print(number_all[j], end="\t")
    if j%3 ==2:
        print("\n")
#  將每條線尚未中獎的數字個數預設為3
for k in range(8):
    line.append(3)
    
while(Bingo != 0):  #  當尚未連線則執行
    #    由使用者輸入中獎號碼
    choice = input("中獎號碼：")
    print()        #換行
    #  若中獎號碼在某直排
    for check_column in range(3):
        if(number_all.index(int(choice)) % 3 == check_column):
                line[check_column] -= 1
    #  若中獎號碼在某橫排
    for check_row in range(3):
        if(number_all.index(int(choice)) // 3 == check_row):
                line[check_row+3] -= 1
    #  若中獎號碼在斜排
    if(number_all.index(int(choice)) == 0):
        line[6] -= 1
    elif(number_all.index(int(choice)) % 4 == 0):
        line[6] -= 1
        line[7] -= 1
    elif(number_all.index(int(choice)) % 2 == 0 ):
        line[7] -= 1
    
    #  判斷是否連線(若連線則變數Bingo == 0)
    for l in range(8):
        Bingo *= line[l]
print("Bingo！")    #  連線後不繼續執行迴圈則印出「Bingo！」