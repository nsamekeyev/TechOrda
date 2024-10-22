#5.Напишите программу для нахождения всех совершенных чисел (чисел, равных сумме своих делителей, исключая само число) в заданном диапазоне. Диапазон от 0 до 1000

# Функция для поиска делителей числа
def divisors_sum(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

# Поиск совершенных чисел в заданном диапазоне
def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if num == divisors_sum(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Диапазон поиска
start = 0
end = 1000

# Вывод совершенных чисел в диапазоне
perfect_nums = perfect_numbers_in_range(start, end)
print(f"Совершенные числа в диапазоне от {start} до {end}: {perfect_nums}")

