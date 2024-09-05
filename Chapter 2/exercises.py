# №2
# PROFIT_PART = 0.23
# all_cash = input('Введите общую выручку: ')
# profit = float(all_cash) * PROFIT_PART
# print(f'Прибыль компании составляет: {profit}')

# №3

# square = float(input('Введите общую площадь земли в кв. метрах: '))
# print(f'Площадь земли в акрах равна: {square / 4047}')

# №4
# purchase1 = float(input('Введите стоимость товара 1: '))
# purchase2 = float(input('Введите стоимость товара 2: '))
# purchase3 = float(input('Введите стоимость товара 3: '))
# purchase4 = float(input('Введите стоимость товара 4: '))
# purchase5 = float(input('Введите стоимость товара 5: '))
# p_summ = purchase1 + purchase2 + purchase3 + purchase4 + purchase5
# tax = p_summ * 0.07
# total_summ = tax + p_summ
# print(f'Сумма всех товаров равна: {p_summ}')
# print(f'Налог с суммы равен: {tax:.2f}')
# print(f'Итого за покупку: {total_summ}')

# №5
# AUTO_SPEED = 70
# print(f'Расстояние за 6 часов составляет: {AUTO_SPEED * 6} км')
# print(f'Расстояние за 10 часов составляет: {AUTO_SPEED * 10} км')
# print(f'Расстояние за 15 часов состоавляет: {AUTO_SPEED * 15} км')

# №6

# buy_summ = float(input('Введите общую сумму покупки: '))
# federal_tax = buy_summ * 0.05
# region_tax = buy_summ * 0.025
# overall_tax = federal_tax + region_tax
# final_summ = buy_summ + overall_tax
# print(f'Сумма покупки составляет: {buy_summ:.2f}')
# print(f'Федеральный налог с продаж составляет: {federal_tax:.2f}')
# print(f'Региональный налог с продаж составляет: {region_tax:.2f}')
# print(f'Общий налог с продаж составляет: {overall_tax:.2f}')
# print(f'Общая сумма покупки составляет: {final_summ:.2f}')

# №8

# summ = float(input('Введите стоимость всей еды: '))
# tips = summ * 0.18
# sell_tax = summ * 0.07
# total = summ + tips + sell_tax
# print(f'Стоимость еды равна: {summ:.2f}')
# print(f'Чаевые составляют: {tips:.2f}')
# print(f'Налог с продаж составляет: {sell_tax:.2f}')
# print(f'Общая сумма равна: {total:.2f}')

# №9

# celsium = float(input('Введите температуру в цельсиях: '))
# farengheit = ((9 * celsium) / 5) + 32
# print(f'Температура по фаренгейту равна: {farengheit:.2f}')

# №10

# one_cake_sugar = 1.5 / 48
# one_cake_oil = 1 / 48
# one_cake_flour = 2.75 / 48
# cake_number = float(input('Введите желаемое количество булочек: '))
# print(f'Для этого количества булочек необходимо: \n'
#       f'{one_cake_sugar * cake_number:.1f} стакана сахара \n'
#       f'{one_cake_oil * cake_number:.1f} стакана масла \n'
#       f'{one_cake_flour * cake_number:.1f} стакана муки')

# №11

# male = float(input('Введите количество мальчиков: '))
# female = float(input('Введите количество девочек: '))
# male_percent = (male / (male + female))
# female_percent = (female / (male + female))
# print(f'Процент мальчиков равен: {male_percent:.0%}')
# print(f'Процент девочек равен: {female_percent:.0%}')

# №12

# akcii = 2000
# price_buy = 40.0
# tax_buy = (akcii * price_buy) * 0.03
# price_cell = 42.75
# buy_summ = akcii * price_buy
# cell_summ = akcii * price_cell
# tax_cell = cell_summ * 0.03
# final_total = cell_summ - buy_summ - (tax_buy + tax_cell) 
# print(f'Акции куплены за {buy_summ:.2f} рублей')
# print(f'Комиссия покупки равна {tax_buy:.2f} рублей')
# print(f'Акции проданы за {cell_summ:.2f} рублей')
# print(f'Комиссия продажи равна {tax_cell:.2f} рублей')
# print(f'Итоговый профит: {final_total:.2f} рублей')

# №13

# R = float(input('Введите длину гряды в метрах: '))
# E = float(input('Введите размер пространства в метрах: '))
# S = float(input('Введите расстояние между виноградными лозами в метрах: '))
# V = (R - (2 * E)) / S
# print(f'Количество виноградных лоз составляет: {V:.0f} штук')

# №14
# P = float(input('Введите основную первоначальную сумму: '))
# r = float(input('Введите процентную ставку: '))
# n = float(input('Введите частоту начисления процентов : '))
# t = float(input('Введите количество лет хранения вклада: '))
# A = P * ((1 + (r / n))) ** (n * t)
# print(f'Итоговая сумма денег составляет: {A:.2f}')