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

# MIN = 1
# MAX = 6

# def main():
#     again = 'y'

#     while again == 'y' or again == 'Y':
#         print('Выпали следующие кубики: ')
#         print(random.randint(MIN, MAX), random.randint(MIN, MAX))
#         again = input('Сделать еще один бросок (y/n)?: ')
# main()

# HEADS = 1
# TAILS = 2
# TOSSES = 10

# def main():
#     for toss in range(TOSSES):
#         if random.randint(HEADS, TAILS) == HEADS:
#             print('Орёл')
#         else:
#             print('Решка')

# main()
# random.seed(10)
# a = random.randint(1, 100)
# b = random.randint(1, 100)
# print(a, b)

# def main():
#     first_age = int(input('Введите свой возраст: '))
#     second_age = int(input('Введите возраст своего лучшего друга: '))

#     total = sum(first_age, second_age)
#     print(f'Вместе вам {total} лет.')

# def sum(num1, num2):
#     result = num1 + num2
#     return result

# main()

# DISCOUNT_PERCENTAGE = 0.20

# def main():
#     reg_price = get_regular_price()

#     sale_price = reg_price - discount(reg_price)

#     print(f'Отпускная цена составляет {sale_price:,.2f}')

# def get_regular_price():
#     price = float(input('Введите обычную цену товара: '))
#     return price

# def discount(price):
#     return price * DISCOUNT_PERCENTAGE

# main()

