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