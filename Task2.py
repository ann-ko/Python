# Создаем список
list_l = list()

size_list = int(input("Введите размер списка: "))

if size_list > 0:
    # ввод данных пользователем
    for i in range(size_list):
        new_value = input("Введите значение для списка: ")
        list_l.append(new_value)

print("Исходный список: ", list_l)

# Реализуем обмен значений соседних элементов
for i in range(size_list)[::2]:
    if i != size_list - 1:  # Для всех элементов кроме последнего если размер нечетный
        list_l[i], list_l[i+1] = list_l[i+1], list_l[i]  # обмен значений

print("Измененный список: ", list_l)
