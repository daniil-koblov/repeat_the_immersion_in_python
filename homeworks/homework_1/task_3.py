nums = int(input('Введите количество чисел: '))
count = 0
for i in range(nums):
    num = int(input('Введите число: '))
    for j in range(2, nums):
        if num > 1:
            if num % j == 0:
                break
    count += 1
print(f'Количество простых чисел в последовательности равно: {count}.')
