# keep_going = 'д'
# while keep_going == 'д':
#     sales = float(input('Введите объём продаж: '))
#     comm_rate = float(input('Введите ставку комиссионных: '))
#     commission = sales * comm_rate
#     print(f'Комиссионное вознаграждение составляет ${commission:,.2f}.')
#     keep_going = input('Хотите вычислить еще одно ' + 
#                        '(Введите "д", если да): ')
    
# MAX_TEMP = 102.5
# temperature = float(input('Введите температуру вещества в градусах Цельсия: '))
# while temperature > MAX_TEMP:
#     print('Температура слишком высокая')
#     print('Убавьте нагрев и подождите')
#     print('5 минут. Затем снимите показание температуры')
#     print('снова и введите полученное значение.')
#     temperature = float(input('Введите новое показание температуры: '))
# print('Температура приемлемая')
# print('Проверьте снова показание температуры через 15 минут')

# print('Я покажу числа от 1 до 5')
# for num in [1, 2, 3, 4, 5]:
#     print(num)


# for name in ['Мигнуть', 'Моргнуть', 'Кивнуть']:
#     print(name)

# print('Я покажу числа от 1 до 5')
# for num in range(5):
#     print(num)

# for x in range(5):
#     print('Привет, Мир!')


# print('Я покажу числа от 1 до 5')
# for num in range(1, 6):
#     print(num)

# for num in range(1, 10, 2):
#     print(num)

# print('Число\tКвадрат числа')
# print('-----------------------')
# for number in range(1, 11):
#     square = number**2
#     print(f'{number}\t{square}')

# START_SPEED = 60
# END_SPEED = 131
# INCREMENT = 10
# CONVERSATION_FACTOR = 0.6214
# print('\n')
# print('KPH\tMPH')
# print('--------------------------------')
# for kph in range(START_SPEED, END_SPEED, INCREMENT):
#     mph = kph * CONVERSATION_FACTOR
#     print(f'{kph}\t{mph:.1f}')

# print('Эта программа выводит список чисел, '
#       'начиная с 1 и их квадраты')
# end = int(input('введите крайнее число диапазона: '))
# print()
# print('Число\tКвадрат числа')
# print('-----------------------')
# for number in range(1, end + 1):
#     square = number**2
#     print(f'{number}\t{square}')


# print('Эта программа выводит список чисел, '
#       'и их квадраты')
# start = int(input('Введите первое число диапазона: '))
# end = int(input('Введите крайнее число диапазона: '))
# print()
# print('Число\tКвадрат числа')
# print('-----------------------')
# for number in range(start, end + 1):
#     square = number**2
#     print(f'{number}\t{square}')

# for num in range(10, 5, -1):
#     print(num)

# MAX = 5
# total = 0.0
# print(f'Эта программа вычисляет сумму из {MAX} чисел, которые вы введёте.')
# for counter in range(5):
#     number = float(input('Введите число: '))
#     total = total + number
# print(f'Сумма составляет {total}.')


# TAX_FACTOR = 0.0065
# print('Введите номер имущественного лота либо 0, чтобы завершить.')
# lot = int(input('Номер лота: '))

# while lot != 0:
#     value = float(input('Введите стоимость имущества: '))
    
#     tax = value * TAX_FACTOR

#     print(f'Налог на имущество: ${tax:,.2f}')
#     print('Введите следующий номер имущественного лота либо 0, чтобы завершить.')
#     lot = int(input('Номер лота: '))


# from time import sleep

# for seconds in range(1, 61):
#     print(seconds)

# for minutes in range(60):
#     for seconds in range(60):
#         sleep(1)
#         print(minutes, ':', seconds)


# num_students = int(input('Сколько у вас студентов? '))
# num_test_scores = int(input('Сколько оценок в расчёте на одного студента? '))
# for student in range(num_students):
#     total = 0.0
#     print('Номер студента', student + 1)
#     print('------------------')

#     for test_num in range(num_test_scores):
#         print(f'Номер лабораторной работы {test_num + 1}', end='')
#         score = float(input(': '))
#         total += score

#     average = total / num_test_scores
#     print(f'Средний балл студента номер {student + 1} составляет: {average:.1f}')
#     print()

# for str in range(8):
    
    
#     for col in range(6):
#         print('*', end='   ')
#     print()

# for r in range(8):
#     for c in range(r):
#         print(' ', end='')
#     print('#')

import turtle
# turtle.speed(1)
# for x in range(8):
#     turtle.forward(100)
#     turtle.right(45)
# turtle.done()

# NUM_CIRCLES = 20
# STARTING_RADIUS = 20
# OFFSET = 10
# ANIMATION_SPEED = 1

# turtle.speed(ANIMATION_SPEED)
# # turtle.hideturtle()

# radius = STARTING_RADIUS

# for count in range(NUM_CIRCLES):
#     turtle.circle(radius)
#     x = turtle.xcor()
#     y = turtle.ycor() - OFFSET
#     radius = radius + OFFSET

#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
# turtle.done()

# NUM_CIRCLES = 10
# RADIUS = 150
# ANGLE = 36
# ANIMATION_SPEED = 8

# turtle.speed(ANIMATION_SPEED)
# for x in range(NUM_CIRCLES):
#     turtle.circle(RADIUS)
#     turtle.left(ANGLE)
# turtle.done()

START_X = -200
START_Y = -100
NUM_LINES = 5
LINE_LENGTH = 400
ANGLE = 144
ANIMATION_SPEED = 3

turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
turtle.left(36)
turtle.bgcolor('blue')

for x in range(NUM_LINES):
    
    turtle.pencolor('pink')
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)
    
turtle.done()