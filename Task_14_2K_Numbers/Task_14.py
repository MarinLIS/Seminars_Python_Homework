# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int (input ("Введите число: "))
i = 0
counter = 0
while counter <= n:
    counter=2**i
    if counter > n:
        break
    i+=1
    print (counter, end =" ")

