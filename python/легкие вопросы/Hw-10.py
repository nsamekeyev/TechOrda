 ##sort Реализовать функцию sort, которая принимает массив array(int[]). Функция должна отсортировать массив по возрастанию. Подсказка: https://habr.com/ru/post/204600/ Запрещено использовать Arrays.sort. Пример int array[] = {7, 5, 9, 1, 4}; sort(array);

def sort_array(array):
    # Реализуем пузырьковую сортировку
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Меняем элементы местами, если текущий элемент больше следующего
                array[j], array[j+1] = array[j+1], array[j]

array = [7, 5, 9, 1, 4]
sort_array(array)
print(array)  # Ожидаемый вывод: [1, 4, 5, 7, 9]

