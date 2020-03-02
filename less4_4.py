my_list = [43, 65, 43, 21, 94, 21, 8, 111, 8, 10]
new_list = [element for element in my_list if my_list.count(element) < 2]
print("Элементы списка, не имеющие повторений:", new_list)
