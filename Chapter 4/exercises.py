# №1
# product = 1
# while product < 100:
#     number = float(input('Введите число: '))
#     product = number * 10


# again = 'д'
# while again == 'д':
#     number1 = float(input('Введите первое число: '))
#     number2 = float(input('Введите второе число: '))
#     print(f'Результат их сложения равен: {number1 + number2}')
#     again = input('Если хотите еще раз, введите "д": ')
# print('Программа завершена')

# for num in range(0, 1001, 10):
#     print(num)

# total = 0.0
# for num in range (10):
#     data = int(input('Введите число: '))
#     total += data
# print(total)

# total = 0.0
# for num in range(1, 31):
#     total += (num / (31 - num))
# print(total)

# for string in range(10):
#     for sign in range(15):
#         print('#', end=' ')
#     print()

# x = int(input('Введите число больше нуля: '))
# while x <= 0:
#     x = float(input('Ошибка! Введите положительное число: '))
    
    
# x = int(input('Введите число от 1 до 100: '))
# while x < 1 or x > 100:
#     x = float(input('Ошибка! Не верный диапазон: '))

# bugs_total = 0.0
# for days in range(5):
#     bugs_a_day = float(input(f'Введите количество ошибок за {days + 1}-й день: '))
#     bugs_total += bugs_a_day
# print(f'Количество ошибок за 5 дней составляет: {bugs_total:.1f}')

# for minutes in range(10, 31, 5):
#     burned_calories = minutes * 4.2
#     print(f'Количество сожжёных калорий за {minutes} минут бега составляет: {burned_calories}')

# budget = float(input('Введите ваш бюджет на месяц: '))
# pay_types = int(input('Сколько статей расхода у вас было в этом месяце: '))
# month_total = 0.0
# for count in range(pay_types):
#     pay_type = float(input(f'Расход по {count + 1} статье: '))
#     month_total += pay_type

# if month_total > budget:
#     print(f'Вы перерасходовали {month_total - budget} рублей')
# else:
#     print(f'Вы сэкномили {budget - month_total} рублей')

# distance = 0.0
# speed = int(input('Введите скорость транспортного средства в км/ч: '))
# hours = int(input('Сколько часов оно двигалось с такой скоростью?: '))
# print()
# print('Час\tПройденное расстояние')
# print('-----------------------------')
# for hour in range(hours):
#     print(f'{hour+1}\t{(hour + 1) * speed} км')

#Ex5
# years = int(input('Введите количество лет в периоде: '))
# total_rain = 0.0
# for year in range(years):
#     print(f'Осадки за {year + 1}-й год')
#     for month in range(12):
#         rain_month = int(input(f'Введите количество осадков за {month + 1}-й месяц: '))
#         total_rain += rain_month
# print(f'Итого:\n'
#       f'Количество месяцев составляет: {years * 12}\n'
#       f'Общее количество осадков за период составляет: {total_rain}\n'
#       f'Среднее количество осадков в месяц за весь период составляет: {total_rain / (years * 12)}')

#Ex6

# print('Celcium\t\tFarengheit')
# print('--------------------------')

# for cel in range(21):
#     far = ((9 / 5) * cel) + 32
#     print(f'{cel}\t\t{far:.1f}')

#Ex7

# days = int(input('Введите количество отработанных дней: '))
# print('День\tЗарплата')
# print('-------------------')
# print('1\t1')
# salary = 1
# for day in range(days - 1):
#     salary *= 2
#     print(f'{day + 2}\t{salary}')
# print(f'Итоговая зарплата в рублях составит {(salary / 100)} рублей')

#Ex8

# total = 0.0
# digit = int(input('Введите число для подсчёта суммы, либо отрицательное для завершения: '))
# while digit >= 0:
#     total += digit
#     digit = int(input('Введите следующее число для подсчёта суммы, либо отрицательное для завершения: '))
# print(f'Сумма всех введённых чисел составляет: {total}')

#Ex9
# level = 0.0
# print('Год\tУровень, мм')
# print('--------------------')
# for n in range(1, 26):
#     level += 1.6
#     print(f'{n}\t{level:.2f}')

#Ex10
# cost_a_year = 290000
# print('Год\tЦена')
# print('----------------')
# print('1\t290000')
# for n in range(2, 6):
#     cost_a_year = (0.03 * cost_a_year) + cost_a_year
#     print(f'{n}\t{cost_a_year:.2f}')

#Ex11
# weight = float(input('Введите ваш вес: '))
# print('Месяц\tВес')
# print('----------------')
# for n in range(1, 6):
#     weight -= 1.5 
#     print(f'{n}\t{weight:.2f}')

#Ex12
# weight = int(input('Введите число для вычисления факториала: '))
# for n in range(1, weight):
#     weight *= n
# print(weight)

#Ex13
# start_population = int(input('Введите стартовое количество популяции: '))
# grow_percent = float(input('Введите среднесуточный прирост в процентах: '))
# days_count = int(input('Введите количество дней: '))
# print('День\tПопуляция')
# print('-------------------')
# total_population = (start_population * grow_percent) + start_population
# print(f'1\t{total_population}')

# for n in range(2, days_count + 1):
#     total_population = (total_population * grow_percent) + total_population
#     print(f'{n}\t{total_population:.2f}')

#Ex14

# for r in range(6, 0, -1):
#     for c in range(r):
#         print('*', end='  ')
#     print()

# Ex15

# for r in range(6):
#     print('#', end=' ')
#     for c in range(r):
#         print('', end=' ')
#     print('#')

# Ex16

import turtle

# NUM_SQUARES = 50
# OFFSET = 10
# ANIMATION_SPEED = 100
# x = 1000
# y = -500

# turtle.speed(ANIMATION_SPEED)
# turtle.hideturtle()

# side_lengh = 1000.0


# for r in range(NUM_SQUARES):
#     side_lengh -= (2 * OFFSET)
#     x -= OFFSET
#     y += OFFSET
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     if (r % 2) == 0:
#         turtle.fillcolor('red')
#     else:
#         turtle.fillcolor('green')
#     turtle.begin_fill()

#     for n in range(4):
#             turtle.left(90)
#             turtle.forward(side_lengh)

#     turtle.end_fill()

#Ex17

# START_X = -200
# START_Y = -100
# NUM_LINES = 8
# LINE_LENGTH = 400
# ANGLE = 135
# ANIMATION_SPEED = 15

# turtle.penup()
# turtle.goto(START_X, START_Y)
# turtle.pendown()



# for x in range(NUM_LINES):
#     turtle.pencolor('green')
#     turtle.forward(LINE_LENGTH)
#     turtle.left(ANGLE)
    
# turtle.done()

#Ex18

# NUM_SQUARES = 50
# OFFSET = 10
# ANIMATION_SPEED = 5

# turtle.speed(ANIMATION_SPEED)
# turtle.hideturtle()
# turtle.left(90)
# side_lengh = 0


# for r in range(NUM_SQUARES):
#     side_lengh += 5

#     for n in range(2):
#             turtle.forward(side_lengh)
#             turtle.left(90)
#             turtle.forward(2 * side_lengh)

# #Ex19



# turtle.hideturtle()

# side_lengh = 1000.0


# for r in range(NUM_SQUARES):
#     side_lengh -= (2 * OFFSET)
#     x -= OFFSET
#     y += OFFSET
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     if (r % 2) == 0:
#         turtle.fillcolor('red')
#     else:
#         turtle.fillcolor('green')
#     turtle.begin_fill()

#     for n in range(4):
#             turtle.left(90)
#             turtle.forward(side_lengh)

# turtle.hideturtle()
# turtle.penup()
# turtle.goto(-100, -50)
# turtle.pendown()
# turtle.left(90)
# turtle.speed(5)

# for x in range(8):
#     turtle.forward(100)
#     turtle.right(45)

# turtle.penup()
# turtle.goto(7, 0)
# turtle.pendown()
# turtle.write('STOP')
# turtle.done()