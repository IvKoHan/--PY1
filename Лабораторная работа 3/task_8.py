money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
decline = spend - salary  # задолжность по растратам после зарплаты

while money_capital > decline:
    money_capital -= decline
    spend *= 1 + increase
    decline = spend - salary
    month += 1

print(month)
