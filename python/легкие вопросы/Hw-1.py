#Условия ##int-cmp Дается два числа a и b. Вернуть: 1, если a > b 0, если a = b -1, если a < b Sample Input: 1 0 Sample Output: 1

def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

a, b = map(int, input("Введите два числа через пробел: ").split())
result = int_cmp(a, b)
print(result)

