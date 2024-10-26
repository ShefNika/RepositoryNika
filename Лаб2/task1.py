money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
k = 0

while spend < money_capital + salary:
    money_capital -= (spend - salary)
    spend *= (1 + increase)
    k += 1
print("Количество месяцев, которое можно протянуть без долгов:", k)
