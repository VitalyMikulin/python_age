HIGH_SCORE = 95
test1 = int(input('Введите оценку 1: '))
test2 = int(input('Введите оценку 2: '))
test3 = int(input('Введите оценку 3: '))
average = (test1 + test2 + test3) / 3
print(f'Средний балл составляет: {average:.0f}')
if average >= HIGH_SCORE
    print('Поздравляем!')
    print('Отличный средний балл')