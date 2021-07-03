list_t = list()
list_t.append("первый элемент")
list_t.append(2019)
list_t.append(3.14)
list_t.append([1, 2, 3])
list_t.append((1, 2, 3))
list_t.append({1, 2, 3})
list_t.append({1: 10, 2: 20, 3: 30})
list_t.append(True)
list_t.append(None)
print("Список для анализа: ", list_t)
print("Определяем типы данных всех элементов в списке:")
for i in list_t:
    print(f"type of {i} = {type(i)}")
print("Ищем в скрипте элементы типа tuple и set:")
for i in list_t:
    if (type(i) == tuple) or (type(i) == set):
        print(f"type of {i} = {type(i)}")