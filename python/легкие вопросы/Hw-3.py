 #Циклы ##sqr-sum-1-n Вернуть сумму квадратов чисел от 1 до n включительно. Ограничения 1 <= n <= 10860

def sqr_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

n = int(input("Введите число n: "))
if 1 <= n <= 10860:
    result = sqr_sum(n)
    print(result)
else:
    print("Введите значение n в диапазоне от 1 до 10860.")

