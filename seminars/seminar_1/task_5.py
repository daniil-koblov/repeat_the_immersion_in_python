n = int(input('Введите число: '))
e = int(input('Введите число: '))

step = 1
count = 1
sum_num = 0

while count <= n:
    if count % e == 0:
        count += step
        continue
    else:
        sum_num += count
        count += step

print(sum_num)
