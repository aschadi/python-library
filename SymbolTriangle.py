symbol = input('What symbol to use? ')
nb_lines = int(input('How many lines? '))

for i in range(0, nb_lines, 1):
    for j in range(nb_lines - 1, i, -1):
        print(' ', end='')
    for k in range(0, (2 * i) + 1, 1):
        print(symbol, end='')
    print('\n')
