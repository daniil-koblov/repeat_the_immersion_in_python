FIRST_NUM = 1
LAST_NUM = 999
FIRST_TWO_DIGIT_NUM = 10
FIRST_THREE_DIGIT_NUM = 100
SQUARE_DEGREE = 2

while True:
    input_num = int(input('Введите число в диапазоне от 1 до 999: '))
    if input_num < FIRST_NUM or input_num > LAST_NUM:
        continue
    else:
        break


def num_processing(num):
    result = 0
    if num < FIRST_TWO_DIGIT_NUM:
        result = num ** SQUARE_DEGREE
    elif num < FIRST_THREE_DIGIT_NUM:
        result = (num % FIRST_TWO_DIGIT_NUM
                  * num // FIRST_TWO_DIGIT_NUM)
    else:
        result = num // FIRST_THREE_DIGIT_NUM
        result += ((input_num % FIRST_THREE_DIGIT_NUM) //
                   FIRST_TWO_DIGIT_NUM) * FIRST_TWO_DIGIT_NUM
        result += (((input_num % FIRST_THREE_DIGIT_NUM) % FIRST_TWO_DIGIT_NUM)
                   * FIRST_THREE_DIGIT_NUM)
    return result


print(f'Вы ввели число {input_num}. Результат обработки числа'
      f' {num_processing(input_num)}.')
