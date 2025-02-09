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
#     price = 40
#     return price

# def discount(price):
#     return price * DISCOUNT_PERCENTAGE

# main()

# def is_even(number):
#     if (number % 2) == 0:
#         status = True
#     else:
#         status = False
#     return status

# number = int(input('Введите число: '))
# if is_even(number):
#     print('Это чётное число')
# else:
#     print('Это нечётное число')




# fama, imechko = get_name()

# def get_name():
#     fam = 20
#     imya = 30
#     return fam, imya

# print(fama, imechko)


# import circle
# import rectangle

# AREA_CIRCLE_CHOICE = 1
# CIRCUMFERENCE_CHOICE = 2
# AREA_RECTANGLE_CHOICE = 3
# PERIMETER_RECTANGLE_CHOICE = 4
# QUIT_CHOICE = 5

# def main():
#     choice = 0
#     while choice != QUIT_CHOICE:
#         display_menu()

#         choice = int(input('Выберите вариант: '))

#         if choice == AREA_CIRCLE_CHOICE:
#             radius = float(input('Введите радиус: '))
#             print('Площадь курга равна', circle.area(radius))
#         elif choice == CIRCUMFERENCE_CHOICE:
#             radius = float(input('Введите радиус: '))
#             print('Длина окружности равна ',
#                   circle.circumference(radius))
#         elif choice == AREA_RECTANGLE_CHOICE:
#             width = float(input('Введите ширину: '))
#             length = float(input('Введите длину: '))
#             print('Площадь равна ', rectangle.area(width, length))
#         elif choice == PERIMETER_RECTANGLE_CHOICE:
#             width = float(input('Введите ширину: '))
#             length = float(input('Введите длину: '))
#             print('Периметр равен ', rectangle.perimeter(width, length))
#         elif choice == QUIT_CHOICE:
#             print('Выходим из программы...')
#         else:
#             print('Ошибка: недопустимый выбор.')

# def display_menu():
#     print('МЕНЮ')
#     print('1. Площадь круга')
#     print('2. Длина окружности')
#     print('3. Площадь прямоугольника')
#     print('4. Периметр прямоугольника')
#     print('5. Выход')

# main()

import turtle

# Квадрат
# def main():
#     turtle.hideturtle()
#     square(100, 0, 50, 'red')
#     square(-150, -100, 200, 'blue')
#     square(-200, 150, 75, 'green')
#     turtle.done()

# def square(x, y, width, color):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.fillcolor(color)
#     turtle.pendown()
#     turtle.begin_fill()
#     for count in range(4):
#         turtle.forward(width)
#         turtle.left(90)
#     turtle.end_fill()


# main()

# Круг

# def main():
#     turtle.hideturtle()
#     circle(0, 0, 100, 'red')
#     circle(-150, -75, 50, 'blue')
#     circle(-200, 150, 75, 'green')
#     turtle.done()

# def circle(x, y, radius, color):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.fillcolor(color)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(radius)
#     turtle.end_fill()

# main()

# Линия

# TOP_X = 0
# TOP_Y = 100
# BASE_LEFT_X = -100
# BASE_LEFT_Y = -100
# BASE_RIGHT_X = 100
# BASE_RIGHT_Y = -100

# def main():
#     turtle.hideturtle()
#     line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
#     line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
#     line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')
#     turtle.done()

# def line(startX, startY, endX, endY, color):
#     turtle.penup()
#     turtle.goto(startX, startY)
#     turtle.pendown()
#     turtle.pencolor(color)
#     turtle.goto(endX, endY)

# main()