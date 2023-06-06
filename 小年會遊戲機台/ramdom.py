import random
list= [1,2,3,4,5,6,7,8,9]


for i in range(9):
    aim= random.choice(list)
    if aim in list:
        print(aim)
        list.remove(aim)
    else:
        val= random.choice(list)


