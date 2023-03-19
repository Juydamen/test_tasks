'''Условие задачи "Самое длинное слово":
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо
оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в
нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.
'''

'''Формат ввода:
В первом элементе кортежа дана длина текста L.

Во втором элементе кортежа записан текст, состоящий из строчных латинских букв
и пробелов. Слово — последовательность букв, не разделённых пробелами.
'''

'''Формат вывода:
В первой строке выведите самое длинное слово.
Во второй строке выведите его длину. Если подходящих слов несколько, выведите
то, которое встречается раньше.
'''

# Пример ввода -> вывода:
inputs = [
    ('19', 'i love segment tree'),   # -> segment, 7
    ('21', 'frog jumps from river')  # -> jumps, 5
]

# тут ваше решение:

for j in inputs:
    g = ''
    q = 0
    r = j[1].split(' ')
    for i in range(len(r)):
        if q < len(r[i]):
            g = r[i]
            q = len(r[i])
    print(f'{g}, {len(g)}')
