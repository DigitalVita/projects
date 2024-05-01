column = input('Enter a column on a chessboard (a-g): ')
row = int(input('Enter a row on a chessboard(1-8): '))

blacks = ['a', 'c', 'e', 'g']
whites = ['b', 'd', 'f', 'h']

if column in blacks or whites and row in range(1, 9):
    if column in blacks and row % 2 != 0:
        print(f'{column + str(row)} is black.')
    elif column in blacks and row % 2 == 0:
        print(f'{column + str(row)} is white.')

    elif column in whites and row % 2 != 0:
        print(f'{column + str(row)} is white.')
    elif column in whites and row % 2 == 0:
        print(f'{column + str(row)} is black.')
else:
    print('Out of range.')