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
BREAD_PACK = 8
SOUSAGE_PACK = 10
men_count = int(input('Введите количество гостей: '))
cakes_perman_count = int(input('Введите количество хот-догов на гостя: '))
hot_dogs_count = men_count * cakes_perman_count

if (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) != 0:
    sousage_bags = ((hot_dogs_count // SOUSAGE_PACK) + 1)
    bread_bags = ((hot_dogs_count // BREAD_PACK) + 1)

elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) != 0:
    sousage_bags = (hot_dogs_count // SOUSAGE_PACK)
    bread_bags = ((hot_dogs_count // BREAD_PACK) + 1)

elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) == 0:
    sousage_bags = ((hot_dogs_count // SOUSAGE_PACK) + 1)
    bread_bags = (hot_dogs_count // BREAD_PACK)

elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) == 0:
    sousage_bags = (hot_dogs_count // SOUSAGE_PACK)
    bread_bags = (hot_dogs_count // BREAD_PACK)


if hot_dogs_count <= BREAD_PACK:
    print('Нужен один пакет с булками и один пакет с сосисками!')
    print('Сосисок останется: ', SOUSAGE_PACK - hot_dogs_count)
    print('Булок останется: ', BREAD_PACK - hot_dogs_count)
elif hot_dogs_count > BREAD_PACK and hot_dogs_count <= SOUSAGE_PACK:
    print('Нужно два пакета с булками и один пакет с сосисками!')
    print('Сосисок останется: ', SOUSAGE_PACK - hot_dogs_count)
    print('Булок останется: ', (2 * BREAD_PACK) - hot_dogs_count)
elif hot_dogs_count == 0:
    print('Ничего не нужно из еды!')
elif hot_dogs_count > SOUSAGE_PACK:
    
    if (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) == 0:
        print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
        print('Сосисок останется: ', hot_dogs_count % SOUSAGE_PACK)
        print('Булок останется: ', hot_dogs_count % BREAD_PACK)
    
    elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) == 0:
        print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
        print('Сосисок останется: ', sousage_bags * SOUSAGE_PACK - hot_dogs_count)
        print('Булок останется: ', hot_dogs_count % BREAD_PACK)
    
    elif (hot_dogs_count % SOUSAGE_PACK) == 0 and (hot_dogs_count % BREAD_PACK) != 0:
        print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
        print('Сосисок останется: ', hot_dogs_count % SOUSAGE_PACK)
        print('Булок останется: ', bread_bags * BREAD_PACK - hot_dogs_count)
    
    elif (hot_dogs_count % SOUSAGE_PACK) != 0 and (hot_dogs_count % BREAD_PACK) != 0:
        print('Нужно', bread_bags, 'пакета с булками и', sousage_bags, 'пакета с сосисками!')
        print('Сосисок останется: ', sousage_bags * SOUSAGE_PACK - hot_dogs_count)
        print('Булок останется: ', bread_bags * BREAD_PACK - hot_dogs_count)

else:
    print('Вы ввели некорректные данные')