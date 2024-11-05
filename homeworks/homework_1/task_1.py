height = int(input('Введите высоту: '))
width = int(input('Введите ширину: '))

for i in range(height):
    print('|', end='')
    if i == 0 or i == height - 1:
        for j in range(width):
            print('-', end='')
    else:
        for j in range(width):
            print(' ', end='')
    print('|')
