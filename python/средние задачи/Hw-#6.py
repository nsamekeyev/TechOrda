#6.Реализуйте программу для проверки, является ли заданное число числом Фибоначчи (число, которое является членом последовательности Фибоначчи). Заданное число 25

import math

# Функция для проверки, является ли число точным квадратом
def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s * s == n

# Функция для проверки, является ли число числом Фибоначчи
def is_fibonacci_number(num):
    # Проверяем условия, описанные выше
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Заданное число
n = 25

# Проверка и вывод результата
if is_fibonacci_number(n):
    print(f"{n} является числом Фибоначчи")
else:
    print(f"{n} не является числом Фибоначчи")

