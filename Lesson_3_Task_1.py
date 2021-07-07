def div(val1, val2):
    try:
        result = val1 / val2
        return result
    except ZeroDivisionError:
        return "Нельзя делить на ноль"


try:
    value1 = float(input("Введите первое число для функции деления: "))
    value2 = float(input("Введите второе число для функции деления: "))
except ValueError:
    print("Нужно было ввести число")
else:
    print(f"Результат функции деления: {div(value1, value2)}")