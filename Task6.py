# предположим, что структура всех словарей в исходных данных одинакова

# шаблон для исходных данных - используем его для ввода данных пользователем
database_template = [
    (0, {'название': '', 'цена': 0, 'количество': 0, 'eд': 'шт.'}),
]

# создаем список для исходных данных
database_list = []

# ввод данных пользователем
nn = 0  # счетчик для элементов в списке
while True:
    new_dict = {}
    for key_i in database_template[0][1].keys():  # ключи берем из шаблона
        new_value = input("Введите значение '" + key_i + "': ")
        # на основании шаблона анализируем необходимость изменения типа
        if isinstance(database_template[0][1][key_i], int):  # если это тип int то преобразуем
            new_value = int(new_value)
        new_dict[key_i] = new_value
    nn += 1
    database_list.append((nn, new_dict))
    # Принимаем решение о продолжении ввода данных
    if input("Для ввода следующего блока данных введите '+', если ввод окончен то любой другой символ: ") != '+':
        break

print("Входные данные: ")
for el in database_list:
    print(el)

# создадим структуру для результата на основании шаблона
output_dict = {}
for key_i in database_template[0][1].keys():
    # будем использовать тип list как в условии задачи хотя правильнее здесь использовать set
    output_dict[key_i] = []

# формируем аналитику о товарах
for i in database_list:  # анализируем каждый элемент в исходном списке
    for key_i in i[1].keys():  # перебираем все ключи в исходном словаре
        new_value = i[1][key_i]  # новое значение для добавления
        if new_value not in output_dict[key_i]:  # если бы использовали set то проверка была бы не нужна
            output_dict[key_i].append(new_value)

print("Выходные данные: ")
for key, value in output_dict.items():
    print(key, ':', value)