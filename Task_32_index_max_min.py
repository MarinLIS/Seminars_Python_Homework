# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def getArr (n):
    import random
    arr1 = [random.randint(-10, 11) for _ in range(n)]
    return arr1


def findIndex(arr1, v, k):
    result_arr = []
    for i in range (len(arr1)):
        if v <= arr1[i] <= k:
            result_arr.append(i)
    return result_arr


n = int (input ("Enter the range of the array: "))
arrToUse = getArr(n)
print (arrToUse)
minn = int (input("Enter mininal value: "))
maxx = int (input("Enter maximal value: "))
result = findIndex(arrToUse, minn, maxx)
print (result)