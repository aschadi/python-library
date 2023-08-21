symbol = input('What symbol to use? ')
nb_lines = input('How many lines? ')

for i in range(0, 10, 1):
    for j in range(9, i, -1):
        print(' ', end='')
    for k in range(0, (2 * i) + 1, 1):
        print(symbol, end='')
    print('\n')
