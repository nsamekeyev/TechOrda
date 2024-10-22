#7.Напишите программу, которая определяет, является ли заданное число совершенным числом (число, равное сумме своих делителей, исключая само число). Выведите сообщение с результатом.

# Функция для нахождения делителей числа (кроме самого числа)
def get_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

# Функция для проверки, является ли число совершенным
def is_perfect_number(num):
    divisors_sum = sum(get_divisors(num))
    return divisors_sum == num

# Заданное число
n = int(input("Введите число: "))

# Проверка и вывод результата
if is_perfect_number(n):
    print(f"{n} является совершенным числом")
else:
    print(f"{n} не является совершенным числом")

