input_year = int(input('Введите год: '))
result = None

if input_year % 4 == 0 and input_year % 100 != 0:
    result = True
elif input_year % 4 == 0 and input_year % 100 == 0 and input_year % 400 == 0:
    result = True
else:
    result = False
print(f'Введенный год {'является' if result == True else 'не является'} '
      f'високосным годом.')
