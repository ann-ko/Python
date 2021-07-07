def power_variant_2(v1, v2):
    if v1 < 0:
        return "Первый параметр должен быть действительным положительным числом"
    if v2 >= 0:
        return "Второй параметр должен быть целым отрицательным числом"
    value = 1 / v1
    result = value
    for i in range(-v2 - 1):
        result *= value
    return result


def power_variant_1(v1, v2):
    # здесь тоже можно сначала проверить правильность введенных чисел
    return v1 ** v2


try:
    x = float(input("Введите действительное положительное число для функции возведения числа в степень: "))
    y = int(input("Введите целое отрицательное число  для функции возведения числа в степень: "))
except ValueError:
    print("Тип числа не верен")
else:
    print(f"Результат возведения числа в степень (вариант № 1): {power_variant_1(x, y)}")
    print(f"Результат возведения числа в степень (вариант № 2): {power_variant_2(x, y)}")