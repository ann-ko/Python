def output_info(name, surname, year, city, email, phone):
    print(f"Имя: {name} Фамилия: {surname} Год рождения: {year} Город: {city} email: {email} Телефон: {phone}")


# Для тестирования изменяем последовательность параметров. На экране они должны остаться в прежней последовательности
output_info(phone="9160123104", name="Анна", surname="Косякова", year=1986, city="Канны", email="anna.kosyakova@f-karta.ru")