# №1
# day = float(input('Введите число от 1 до 7: '))
# if day < 1 or day > 7:
#     print('Вы ввели неверное число.')
# elif day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')
# else:
#     print('Вы ввели неверное число.') 

# №2
# side_A_sq_1 = float(input('Введите сторону A прямоугольника 1: '))
# side_B_sq_1 = float(input('Введите сторону B прямоугольника 1: '))
# side_A_sq_2 = float(input('Введите сторону A прямоугольника 2: '))
# side_B_sq_2 = float(input('Введите сторону B прямоугольника 2: '))

# summ_1 = side_A_sq_1 * side_B_sq_1
# summ_2 = side_A_sq_2 * side_B_sq_2

# if summ_1 > summ_2:
#     print('Площадь прямоугольника 1 больше площади прямоугольника 2')
# elif summ_1 < summ_2:
#     print('Площадь прямоугольника 2 больше площади прямоугольника 1')
# else:
#     print('Площади прямоугольников равны')

# №3

# age = float(input('Введите возраст человека: '))
# if age <= 1:
#     print('Это младенец.')
# elif age > 1 and age < 13:
#     print('Это ребёнок.')
# elif age >= 13 and age < 20:
#     print('Это подросток.')
# else:
#     print('Это взрослый.')

# №4

# number = int(input('Введите число от 1 до 10: '))
# if number == 1:
#     print('I')
# elif number == 2:
#     print('II')
# elif number == 3:
#     print('III')
# elif number == 4:
#     print('IV')
# elif number == 5:
#     print('V')
# elif number == 6:
#     print('VI')
# elif number == 7:
#     print('VII')
# elif number == 8:
#     print('VIII')
# elif number == 9:
#     print('IX')
# elif number == 10:
#     print('X')
# else:
#     print('Вы ввели не верные данные')

# №5
# first_color = input('Введите первый цвет: ')
# second_color = input('Введите второй цвет: ')
# if (first_color == 'синий' and second_color == 'красный') or (first_color == 'красный' and second_color == 'синий'):
#     print('фиолетовый')
# elif (first_color == 'красный' and second_color == 'желтый') or (first_color == 'желтый' and second_color == 'красный'):
#     print('оранжевый')
# elif (first_color == 'синий' and second_color == 'желтый') or (first_color == 'желтый' and second_color == 'синий'):
#     print('зеленый')
# else:
#     print('вы ввели не правильные данные')

# №8
# BREAD_PACK = 8
# SOUSAGE_PACK = 10
# men_count = int(input('Введите количество гостей: '))
# cakes_perman_count = int(input('Введите количество хот-догов на гостя: '))
# hot_dogs_count = men_count * cakes_perman_count

# if men_count < 0 or cakes_perman_count < 0:
#         print('Вы ввели некорректные данные')
#         exit()


# if (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) != 0:
#     sousage_bags = ((hot_dogs_count // SOUSAGE_PACK) + 1)
#     bread_bags = ((hot_dogs_count // BREAD_PACK) + 1)

# elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) != 0:
#     sousage_bags = (hot_dogs_count // SOUSAGE_PACK)
#     bread_bags = ((hot_dogs_count // BREAD_PACK) + 1)

# elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) == 0:
#     sousage_bags = ((hot_dogs_count // SOUSAGE_PACK) + 1)
#     bread_bags = (hot_dogs_count // BREAD_PACK)

# elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) == 0:
#     sousage_bags = (hot_dogs_count // SOUSAGE_PACK)
#     bread_bags = (hot_dogs_count // BREAD_PACK)

# if hot_dogs_count == 0 and cakes_perman_count >= 0 and men_count >= 0:
#     print('Ничего не нужно из еды!')

# elif hot_dogs_count <= BREAD_PACK and hot_dogs_count > 0:
#     print('Нужен один пакет с булками и один пакет с сосисками!')
#     print('Сосисок останется: ', SOUSAGE_PACK - hot_dogs_count)
#     print('Булок останется: ', BREAD_PACK - hot_dogs_count)
# elif hot_dogs_count > BREAD_PACK and hot_dogs_count <= SOUSAGE_PACK:
#     print('Нужно два пакета с булками и один пакет с сосисками!')
#     print('Сосисок останется: ', SOUSAGE_PACK - hot_dogs_count)
#     print('Булок останется: ', (2 * BREAD_PACK) - hot_dogs_count)


# elif hot_dogs_count > SOUSAGE_PACK:
    
#     if (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) == 0:
#         print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
#         print('Сосисок останется: ', hot_dogs_count % SOUSAGE_PACK)
#         print('Булок останется: ', hot_dogs_count % BREAD_PACK)
    
#     elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) == 0:
#         print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
#         print('Сосисок останется: ', sousage_bags * SOUSAGE_PACK - hot_dogs_count)
#         print('Булок останется: ', hot_dogs_count % BREAD_PACK)
    
#     elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) != 0:
#         print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
#         print('Сосисок останется: ', hot_dogs_count % SOUSAGE_PACK)
#         print('Булок останется: ', bread_bags * BREAD_PACK - hot_dogs_count)
    
#     elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) != 0:
#         print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
#         print('Сосисок останется: ', sousage_bags * SOUSAGE_PACK - hot_dogs_count)
#         print('Булок останется: ', bread_bags * BREAD_PACK - hot_dogs_count)

# №9

# cell = int(input('Введите номер ячейки от 0 до 36: '))
# if cell < 0 or cell > 36:
#     print('Вы ввели неверное значение. Перезапустите программу.')
#     exit()
# elif cell == 0:
#     print('Зелёная')
# elif cell >= 1 and cell <= 10 and cell % 2 == 0:
#     print('Чёрный')
# elif cell >= 1 and cell <= 10 and cell % 2 != 0:
#     print('Красный')
# elif cell >= 11 and cell <= 18 and cell % 2 != 0:
#     print('Чёрный')
# elif cell >= 11 and cell <= 18 and cell % 2 == 0:
#     print('Красный')
# elif cell >= 19 and cell <= 28 and cell % 2 == 0:
#     print('Чёрный')
# elif cell >= 19 and cell <= 28 and cell % 2 != 0:
#     print('Красный')
# elif cell >= 29 and cell <= 36 and cell % 2 != 0:
#     print('Чёрный')
# elif cell >= 29 and cell <= 36 and cell % 2 == 0:
#     print('Красный')

# №10

# coins_5 = int(input('Введите количество монет ценностью 5 копеек: '))
# coins_10 = int(input('Введите количество монет ценностью 10 копеек: '))
# coins_50 = int(input('Введите количество монет ценностью 50 копеек: '))
# if coins_5 < 0 or coins_10 < 0 or coins_50 < 0:
#     print('Введите корректное значение')
# else:
#     summ = (coins_5 * 5) + (coins_10 * 10) + (coins_50 * 50)
#     if summ == 100:
#         print('Поздравляем с выигрышем, вы достигли одного рубля!')
#     elif summ < 100:
#         print('Увы! Ваша сумма монет не достигла одного рубля!')
#     elif summ > 100:
#         print('Увы! Ваша сумма монет превысила один рубль!')

# # № 12
# COST_PER_PACKET = 99
# packet_number = int(input('Введите количество купленных пакетов: '))
# if packet_number < 0:
#     print('Введите положительное число')
#     exit()
# elif packet_number >= 0 and packet_number < 10:
#     summ = packet_number * COST_PER_PACKET
#     print('Ваша сумма скидки = 0')
#     print(f'Ваша сумма к полате с учётом скидки: {summ}')

# elif packet_number >= 10 and packet_number <= 19:
#     summ = packet_number * COST_PER_PACKET
#     off_cost = summ * 0.1
#     customer_summ = summ - off_cost
#     print(f'Ваша сумма скидки = {off_cost:.2f}')
#     print(f'Ваша сумма к полате с учётом скидки: {customer_summ:.2f}')

# elif packet_number >= 20 and packet_number <= 49:
#     summ = packet_number * COST_PER_PACKET
#     off_cost = summ * 0.2
#     customer_summ = summ - off_cost
#     print(f'Ваша сумма скидки = {off_cost:.2f}')
#     print(f'Ваша сумма к полате с учётом скидки: {customer_summ:.2f}')

# elif packet_number >= 50 and packet_number <= 99:
#     summ = packet_number * COST_PER_PACKET
#     off_cost = summ * 0.3
#     customer_summ = summ - off_cost
#     print(f'Ваша сумма скидки = {off_cost:.2f}')
#     print(f'Ваша сумма к полате с учётом скидки: {customer_summ:.2f}')

# elif packet_number >= 100:
#     summ = packet_number * COST_PER_PACKET
#     off_cost = summ * 0.4
#     customer_summ = summ - off_cost
#     print(f'Ваша сумма скидки = {off_cost:.2f}')
#     print(f'Ваша сумма к полате с учётом скидки: {customer_summ:.2f}')

# №15
# MINUTE = 60
# HOUR = 3600
# DAY = 86400
# seconds = int(input('Введите количество секунд: '))
# if seconds < MINUTE:
#     print('Это меньше минуты, тут нечего считать')
# elif seconds >= MINUTE and seconds < HOUR:
#     minute_only = seconds // MINUTE
#     seconds_only = seconds % MINUTE
#     print(f'{seconds} секунд - это {minute_only} минут и {seconds_only} секунд')
# elif seconds >= HOUR and seconds < DAY:
#     hours_only = seconds // HOUR
#     minute_only = (seconds % HOUR) // MINUTE
#     seconds_only = seconds % MINUTE
#     print(f'{seconds} секунд - это {hours_only} часов, {minute_only} минут и {seconds_only} секунд')
# elif seconds >= DAY:
#     day_only = seconds // DAY
#     hours_only = (seconds % DAY) // HOUR
#     minute_only = (seconds % HOUR) // MINUTE
#     seconds_only = seconds % MINUTE
#     print(f'{seconds} секунд - это {day_only} дней, {hours_only} часов, {minute_only} минут и {seconds_only} секунд')

# №16

# year = int(input('Введите год: '))
# if year % 100 == 0 and year % 400 == 0:
#     print('Это високосный год!')
# elif year % 100 != 0 and year % 4 == 0:
#     print('Это високосный год!')
# else:
#     print('Это не високосный год')

# print('Перезагрузите компьютер и попробуйте подключится')
# answer = input('Вы исправили проблему? \n')
# if answer == 'да':
#     exit()
# else:
#     print('Перезагрузите маршрутизатор и попробуйте подключится')
#     answer = input('Вы исправили проблему? \n')
#     if answer == 'да':
#         exit()
#     else:
#         print('Убедитесь, что кабели между маршрутизатором и модемом прочно соединены')
#         answer = input('Вы исправили проблему? \n')
#         if answer == 'да':
#             exit()
#         else:
#             print('Переместите маршрутизатор на новое место')
#             answer = input('Вы исправили проблему? \n')
#             if answer == 'да':
#                 exit()
#             else:
#                 print('Возьмите новый маршрутизатор')
