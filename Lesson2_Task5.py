my_list = [7, 5, 3, 3, 2]  # исходный список
print(f"Исходный рейтинг: {my_list}")

new_value = float(input("Введите новый элемент рейтинга: "))  # тип float для визуального выделения нового элемента

if my_list[-1] >= new_value:  # Если новое число наименьшее то просто добавляем его в конец списка
    my_list.append(new_value)
else:  # иначе ищем число, которое меньше нового и вставляем новое число перед ним
    for ind, value in enumerate(my_list):
        if value < new_value:
            my_list.insert(ind, new_value)
            break

print(f"Текущий рейтинг: {my_list}")
