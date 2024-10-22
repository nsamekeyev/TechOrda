#4.Реализуйте программу, которая определяет, является ли заданная дата корректной (). Выведите соответствующее сообщение. Дата дана в формате “20.01.2002”

from datetime import datetime

# Функция для проверки корректности даты
def is_valid_date(date_str):
    try:
        # Попытка преобразовать строку в объект даты
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        # Если возникла ошибка, значит дата некорректна
        return False

# Запрашиваем у пользователя ввод даты
date_input = input("Введите дату в формате дд.мм.гггг: ")

# Проверяем дату и выводим результат
if is_valid_date(date_input):
    print(f"Дата {date_input} корректна.")
else:
    print(f"Дата {date_input} некорректна.")

