STEP = 2

height_fir = int(input('Введите высоту ели: '))

# for i in range(height_fir):
#     print(' ' * (height_fir - i - 1) + '*' * (2 * i + 1))

for i in range(height_fir):
    # print(f'{'*' * (2 * i + 1):^{2 * height_fir + 1}}')
    print(f'{'*' * (2 * i + 1):/^{2 * height_fir + 1}}')
