##pow-a-b Вернуть число a в степени b. Используя цикл. Ограничения b > 0 a^b входит в ограничения типа int Sample Input: 2 6 Sample Output: 64

def pow_a_b(a, b):
    result = 1  # Начальное значение результата
    for _ in range(b):  # Цикл выполняется b раз
        result *= a  # Умножаем result на a
    return result  # Возвращаем результат

# Пример использования функции
a = int(input("Введите число a: "))
b = int(input("Введите степень b: "))

if b > 0:
    print(pow_a_b(a, b))
else:
    print("Степень b должна быть больше 0.")

