#Ex1

# def main():
#     kiloms = float(input('Введите расстояние в километрах: '))
#     result = kmstomls(kiloms)
#     print (f'{kiloms:.0f} километров - это {result:.2f} миль')

# def kmstomls(kilometers):
#     miles = kilometers * 0.6214
#     return miles

# main()

#Ex2
# def main():
#     buy_summ = float(input('Введите общую сумму покупки: '))
#     ftax = fed_tax(buy_summ)
#     rtax = reg_tax(buy_summ)
#     otax = overall_tax(ftax, rtax)
#     fsum = final_summ(buy_summ, otax)
    
#     print(f'Сумма покупки составляет: {buy_summ:.2f}')
#     print(f'Федеральный налог с продаж составляет: {ftax:.2f}')
#     print(f'Региональный налог с продаж составляет: {rtax:.2f}')
#     print(f'Общий налог с продаж составляет: {otax:.2f}')
#     print(f'Общая сумма покупки составляет: {fsum:.2f}')

# def fed_tax(buy_sum):
#     federal_tax = buy_sum * 0.05
#     return federal_tax

# def reg_tax(buy_sum):
#     region_tax = buy_sum * 0.025
#     return region_tax

# def overall_tax(ftax, rtax):
#     overall_tax = ftax + rtax
#     return overall_tax

# def final_summ(buy_summ, otax):
#     final_summ = buy_summ + otax
#     return final_summ

# main()


#Ex3

# def main():
#     summ = float(input('Введите стоимость вашего жилья: '))
#     ansure_sum = ans_calc(summ)
#     print(f'Рекомендуемая сумма страховки составляет {ansure_sum:.2f} долларов')

# def ans_calc(summ):
#     result = summ * 0.8
#     return result

# main()

#Ex4

# def main():
#     credit = float(input('За кредит в месяц: '))
#     insure = float(input('За страховку в месяц: '))
#     fuel = float(input('За бензин в месяц: '))
#     motor_oil = float(input('За моторное масло: '))
#     tyres = float(input('За шины: '))
#     service = float(input('Сервис: '))

#     month_summ = total_month(credit, insure, fuel, motor_oil, tyres, service)
#     year_summ = 12 * month_summ 
#     print(f'Все расходы на авто в месяц составляют: {month_summ:.2f}')
#     print(f'Все расходы в год составляют: {year_summ:.2f}')

# def total_month(credit, insure, fuel, motor_oil, tyres, service):
#     result = credit + insure + fuel + motor_oil + tyres + service
#     return result

# main()

#Ex5

# def main():
#     real_cost = float(input('Введите стоимость земли: '))
#     tax_cost_sum = tax_cost(real_cost)
#     real_tax_sum = real_tax(tax_cost_sum)

#     print(f'Облагаемая налогом сумма составляет: {tax_cost_sum:.2f}')
#     print(f'Итоговый налог составляет: {real_tax_sum:.2f}')

# def tax_cost(real_cost):
#     result = real_cost * 0.6
#     return result

# def real_tax(tax_cost_sum):
#     result = (tax_cost_sum / 100) * 0.72
#     return result

# main()

#Ex6

# def main():
#     zhiri = float(input('Введите количество грамм съеденных жиров: '))
#     uglevodi = float(input('Введите количество грамм съеденных углеводов: '))

#     cals_zhir = calzhir(zhiri)
#     cals_uglev = caluglev(uglevodi)

#     print(f'Количество полученных калорий от жиров составляет: {cals_zhir:.2f}')
#     print(f'Количество полученных калорий от углеводов составляет: {cals_uglev:.2f}')

# def calzhir(zhiri):
#     result = zhiri * 9
#     return result

# def caluglev(uglevodi):
#     result = uglevodi * 4
#     return result

# main()

#Ex7

# def main():
#     class_a = int(input('Количество проданных билетов класса А: '))
#     class_b = int(input('Количество проданных билетов класса Б: '))
#     class_c = int(input('Количество проданных билетов класса Б: '))

#     sum_a = calc_a(class_a)
#     sum_b = calc_b(class_b)
#     sum_c = calc_c(class_c)

#     total = sum_a + sum_b + sum_c

#     print(f'Общая сумма дохода составляет: {total}')

# def calc_a(class_a):
#     result = class_a * 20
#     return result
    
# def calc_b(class_b):
#     result = class_b * 15
#     return result
    
# def calc_c(class_c):
#     result = class_c * 10
#     return result

# main()

#Ex8

# def main():
#     square = float(input('Введите площадь работ в квадратных метрах: '))
#     paint_price = float(input('Введите цену 5 литровой ёмкости краски: '))

#     paint_tank_qnty = paint_qnty(square)
#     work_hours_qnty = hours_qnty(square)
#     total_paint_price = paint_tank_qnty * paint_price
#     total_work_price = work_hours_qnty * 2000
#     overall_price = total_paint_price + total_work_price

#     print(f'Количество требуемых ёмкостей по 5л: {paint_tank_qnty}')
#     print(f'Количество требуемых рабочих часов: {work_hours_qnty}')
#     print(f'Общая стоимость краски: {total_paint_price}')
#     print(f'Общая стоимость работы: {total_work_price} рублей')
#     print(f'Общие затраты на всё: {overall_price}')


# def paint_qnty(square):
#     qnty = square / 10
#     if qnty < 1:
#         qnty = 1
#     else:
#         qnty = qnty
#     return qnty

# def hours_qnty(square):
#     h_qnty = square * 0.8
#     return h_qnty

# main()


#Ex9

# def main():
#     profit = float(input('Введите объём продаж: '))
#     federal_tx = fed_tax(profit)
#     municipal_tx = mun_tax(profit)
#     total = federal_tx + municipal_tx
#     print(f'Федеральный налог с продаж составляет:{federal_tx:.2f}')
#     print(f'Муниципальный налог с продаж составляет:{municipal_tx:.2f}')
#     print(f'Общий налог с продаж составляет:{total:.2f}')

# def fed_tax(summ):
#     result = summ * 0.05
#     return result

# def mun_tax(summ):
#     result = summ * 0.025
#     return result

# main()

#Ex10

# def main():
#     feet_qty = int(input('Введите количество футов: '))
#     total_inches = feet_to_inches(feet_qty)
#     print(f'{feet_qty} футов - это {total_inches} дюймов')

# def feet_to_inches(feets):
#     result = feets * 12
#     return result

# main()

#Ex11

import random

answer = 'да'
def main():
    first = random.randint(1, 99)
    second = random.randint(1, 99)
    summ = first + second
    print('\n', first,'\n+\n', second, '\n', sep='')
    userSumm = int(input('Введите ответ: '))
    if userSumm == summ:
        print('\nПоздравляю!\nЭто правильный ответ!\n')
    else:
        print('\nК сожалению ты ошибся:(')
        print(f'Правильный ответ {summ}\n')

while (answer == 'да' or answer == 'Да'):
    main()
    answer = input('Если хочешь другой пример, введи "Да": ')