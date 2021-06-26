revenue = int(input("Введите сумму выручки >>> "))
costs = int(input("Введите сумму издержек >>> "))

profit = revenue - costs

if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабельность = {profitability}")

    workers_count = int(input("Укажите количество сотрудников >>> "))

    profit_per_worker = profit / workers_count
    print(f"Прибыль на одного сотрудника = {profit_per_worker}")
else:
    print(f"Убыток = {profit}")