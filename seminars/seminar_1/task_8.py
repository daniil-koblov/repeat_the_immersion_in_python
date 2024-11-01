STEP_1 = 1
STEP_2 = 2

height_fir = int(input('Введите высоту ели: '))

# for i in range(height_fir):
    # print(' ' * (height_fir - i - STEP_1) + '*' * (STEP_2 * i + STEP_1))

for i in range(height_fir):
    # print(f'{'*' * (STEP_2 * i + STEP_1):^{STEP_2 * height_fir + STEP_1}}')
    print(f'{'*' * (STEP_2 * i + STEP_1):/^{STEP_2 * height_fir + STEP_1}}')
