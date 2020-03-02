from functools import reduce


def my_func(even_number, number):
    return even_number * number


print("Список четных значений", [number for number in range(99, 1001) if number % 2 == 0])
print("Результат перемножения всех элементов списка",
      reduce(my_func, [number for number in range(99, 1001) if number % 2 == 0]))
