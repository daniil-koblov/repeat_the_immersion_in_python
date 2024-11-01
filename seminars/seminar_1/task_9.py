for k in (0, 4):
    print('')
    for i in range(2, 11):
        print('')
        for j in range(2 + k, 6 + k):
            print(f'{j}   x {i:3}   = {i * j:4} \t', end='')
