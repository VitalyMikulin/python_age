# def message():
#     print('Я Артур,')
#     print('король британцев')

# message()


# def main():
#     print('У меня для вас известие.')
#     message()
#     print('До свидания!')

# def message():
#     print('Я Артур,')
#     print('король британцев.')

# main()

# def show_double(number):
#     result = number * 2
#     print(result)

# show_double(5.3)

# def main():
#     intro()
#     cups_needed = int(input('Введите число чашек: '))
#     cups_to_ounces(cups_needed)

# def intro():
#     print('Бла бла бла')
#     print()

# def cups_to_ounces(cups):
#     ounces = cups * 8
#     print(f'Это число конвертируется в {ounces} унций')

# main()

# def main():
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     sum(num1, num2)

# def sum(digit1, digit2):
#     summa = digit1 + digit2
#     print(f'Сумма этих двух чисел равняется {summa}')

# main()


# number = 0

# def main():
#     global number
#     number = int(input('Введите число: '))
#     show_number()

# def show_number():
#     print(f'Вы ввели число {number}')

# main()

# CONTRIBUTION_RATE = 0.05

# def main():
#     gross_pay = float(input('Введите заработную плату: '))
#     bonus = float(input('Введите сумму премий: '))
#     show_pay_contrib(gross_pay)
#     show_bonus_contrib(bonus)

# def show_pay_contrib(gross):
#     contrib = gross * CONTRIBUTION_RATE
#     print(f'Взнос исходя из заработной платы ${contrib:,.2f}')

# def show_bonus_contrib(bonus):
#     contrib = bonus * CONTRIBUTION_RATE
#     print(f'Взнос исходя из суммы пермий: ${contrib:,.2f}')

# main()

import random

# def main():
#     for count in range(5):
#         print(f'Число равняется {random.randint(1, 100):^10d}')

# main()

# random.randint(1, 10)

MIN = 1
MAX = 6

def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        print('Выпали следующие кубики: ')
        print(random.randint(MIN, MAX), random.randint(MIN, MAX))
        again = input('Сделать еще один бросок (y/n)?: ')
main()
