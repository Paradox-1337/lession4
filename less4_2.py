my_list = [156, 25, 336, 111, 86, 543, 54, 123]
new_list = [element for number, element in enumerate(my_list) if my_list[number - 1] < my_list[number]]
print("Исходный список:", my_list)
print("Новый список:", new_list)
