#2.Реализуйте программу, которая определяет, является ли введенная пользователем строка палиндромом (читается одинаково слева направо и справа налево). Выведите соответствующее сообщение. s

# ввод строки
s = input("Введите строку: ")

# Приводим строку к одному регистру и удаляем пробелы
s = s.replace(" ", "").lower()

# Проверяем, является ли строка палиндромом
if s == s[::-1]:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")

