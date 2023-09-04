# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:
# a (n) = a(1) + (n-1) * d (разность).
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arithProg (a, b, c):
   arith_prog = []
   for i in range (a, a +(b*c), c):
      arith_prog.append(i)
   return arith_prog

A_1 = int(input ("Enter first element: "))
D = int (input ("Enter difference: "))
n = int (input ("Enter quantity of elements: "))
result = arithProg(A_1, n, D)
print (result)




