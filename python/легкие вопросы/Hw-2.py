##max-of-three Дается три числа a, b и c. Вернуть максимальное число из них. Sample Input: 42 1 0 Sample Output: 42

def max_of_three(a, b, c):
    return max(a, b, c)

a, b, c = map(int, input("Введите три числа через пробел: ").split())
result = max_of_three(a, b, c)
print(result)

