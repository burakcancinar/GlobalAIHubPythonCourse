#Homework 2 - part 1 
list = [1,"ahmet","2",3,"mehmet",2134,124.47,"burak",14,47,8,10]
swapList = print(list[(len(list)//2):] +list[:(len(list)//2)]) #len(list)//2 bize listenin yarılarını bulmamızı sağladı.

#bu durumda birinci yarımız şu şekilde oldu: [1,"ahmet","2",3,"mehmet",2134]
#          ikinci yarımız da şu şekilde oldu: [124.47,"burak",14,47,8,10]
#-------------------------------------------------------------------------------------------------------------------------
#Homework 2 - Part 2

for i in range(int(input("n: "))+1):
    if i % 2 == 0:
        print(i, end=' ')
    else:
        continue

