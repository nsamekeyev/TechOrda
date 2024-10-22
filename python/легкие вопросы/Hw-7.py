#Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0. Ограничения 0 <= array.length <= 10_000 Sample Input: [1, 2, 3] Sample Output: 1

def find_min(array):
    if not array:  # Проверка на пустой массив
        return 0
    return min(array)  # Возвращаем минимальное значение из массива

# Пример использования функции
sample_input = [1, 2, 3]  # Пример входных данных
result = find_min(sample_input)
print(result)  # Ожидаемый вывод: 1

# Пример с пустым массивом
empty_input = []
result_empty = find_min(empty_input)
print(result_empty)  # Ожидаемый вывод: 0

