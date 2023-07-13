C = 0 # Сумма к оплате
tickets = int(input('Введите количество билетов:'))
for age in range(tickets):
    age = int(input('Введите возраст посетителя:'))
    if age < 18:
        C += 0
    if age >= 18:
        C += 990
    if age >= 25:
        C += 1390
if C == 0:
    print('Проход бесплатный')
else:
    print(C)
if tickets > 3:
    discount = C * 10 / 100
    C = C - discount
print('Стоимость билетов с учетом скидки: ', C)



