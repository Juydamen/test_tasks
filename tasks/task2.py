'''Условие задачи "Чётные и нечётные числа":
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
'''

'''Формат ввода:
На вход через пробел подаются три случайных целых числа a, b и c.
'''

'''Формат вывода:
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
'''

# Пример ввода -> вывода:
inputs = [
    '1 2 -3',  # -> FAIL
    '7 11 7',  # -> WIN
    '6 -2 0'   # -> WIN
]

# тут ваше решение:
for i in inputs:
    d = i.split(' ')
    s = [True if int(d[j]) % 2 == 0 else False for j in range(len(d))]
    print('WIN' if len(set(s)) == 1 else 'FAIL')


for i in inputs:
    inp = i.split()
    values = list(map(int, inp))
    n = 0
    enm = 0
    for nu in values:
        if nu in values:
            enm +=1
        n += 1
    if enm == n:
        print('WIN')
    else:
        print('FAIL')
