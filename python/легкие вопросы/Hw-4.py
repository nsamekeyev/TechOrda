##print-even-a-b Вывести в консоль четные числа в диапазоне от a включительно до b включительно. Sample Input: 0 4 Sample Output: 0 2 4

def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=' ')

# Пример использования функции
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

print_even(a, b)

