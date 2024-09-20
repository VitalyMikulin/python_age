# HIGH_SCORE = 95
# test1 = int(input('Введите оценку 1: '))
# test2 = int(input('Введите оценку 2: '))
# test3 = int(input('Введите оценку 3: '))
# average = (test1 + test2 + test3) / 3
# print(f'Средний балл составляет: {average:.0f}')
# if average >= HIGH_SCORE:
#     print('Поздравляем!')
#     print('Отличный средний балл')


# y = int(input('Введите значение для y: '))
# if y >= 10000:
#     x = 0.2
# else:
#     x = 'фак ю'
# print(x)


# BASE_HOURS = 40
# OT_MULTIPLIER = 1.5

# hours = float(input('Введите отработанное количество часов в неделю: '))
# pay_rate = float(input('Введите почасовую ставку: '))
# if hours > BASE_HOURS:
#     overtime_hours = hours - BASE_HOURS
#     overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
#     gross_pay = BASE_HOURS * hours + overtime_pay
# else:
#     gross_pay = BASE_HOURS * hours
# print(f'Зарплата до удержания составляет: ${gross_pay:.2f}')


# password = input('Введите пароль: ')
# if password == 'prospero':
#     print('Пароль принят')
# else:
#     print('Пароль введён неверно')

# name1 = input('Ведите первое имя и фамилию: ')
# name2 = input('Введите вторую имя и фамилию: ')
# if name1 < name2:
#     print(name1)
#     print(name2)
# else:
#     print(name2)
#     print(name1)

# A_SCORE = 90
# B_SCORE = 80
# C_SCORE = 70
# D_SCORE = 60
# score = int(input('Введите ваш балл: '))

# if score >= A_SCORE:
#     print('Ваша оценка "A"')
# else:
#     if score >= B_SCORE:
#         print('Ваша оценка "B"')
#     else:
#         if score >= C_SCORE:
#             print('Ваша оценка "C"')
#         else:
#             if score >= D_SCORE:
#                 print('Ваша оценка "D"')
#             else:
#                 print('Ваша оценка "F"')

number = float(input('Введите число: '))

if number == 1:
    print('Один')
elif number == 2:
    print('Dva')
elif number == 3:
    print('Tri')
else:
    print('Dohrena')