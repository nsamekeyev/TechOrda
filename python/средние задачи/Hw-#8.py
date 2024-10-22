#8.Создайте программу, которая определяет, в какой сезон года попадает заданная дата (месяц и день).

# Функция для определения сезона по месяцу и дню
def determine_season(day, month):
    if (month == 12 and day >= 1) or (month == 1 or month == 2) or (month == 3 and day < 21):
        return "Зима"
    elif (month == 3 and day >= 21) or (month == 4 or month == 5) or (month == 6 and day < 21):
        return "Весна"
    elif (month == 6 and day >= 21) or (month == 7 or month == 8) or (month == 9 and day < 23):
        return "Лето"
    elif (month == 9 and day >= 23) or (month == 10 or month == 11) or (month == 12 and day < 21):
        return "Осень"

# Ввод даты
date = input("Введите дату в формате ДД.ММ (например, 21.06): ")
day, month = map(int, date.split('.'))

# Определение сезона и вывод результата
season = determine_season(day, month)
print(f"Дата {date} попадает в сезон: {season}")

