result = 0
while True:
    print(f"Текущая сумма = {result}")
    input_s = input("Введите строку чисел, разделенных пробелом для подсчета суммы (# - символ для завершения): ")
    input_a = input_s.split()
    for value in input_a:
        if value == "#":
            break
        try:
            result += float(value)
        except ValueError:
            print(f"Значение {value} не было учтено при подсчете суммы - неверный тип")
    else:
        # если символа завершения программы не было, то продолжаем ввод данных
        continue
    # окажемся здесь (стоп) если встретим символ завершения программы
    break

print(f"Окончательная сумма = {result}")
