#1.Создайте программу, которая проверяет, является ли введенное пользователем число четным или нечетным, и выводит соответствующее сообщение.

# ввод числа
number = int(input("Введите число: "))

# Проверяем, является ли число четным или нечетным
if number % 2 == 0:
    print(f"{number} — четное число.")
else:
    print(f"{number} — нечетное число.")

