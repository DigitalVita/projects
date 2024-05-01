sides = int(input('Enter a number of sides (3 to 10): '))

if sides in range(3, 11):
    if sides == 3:
        print('A triangle.')
    elif sides == 4:
        print('A quadrilateral.')
    elif sides == 5:
        print('A pentagon.')
    elif sides == 6:
        print('A hexagon.')
    elif sides == 7:
        print('A heptagon.')
    elif sides == 8:
        print('An octagon.')
    elif sides == 9:
        print('A nonagon.')
    elif sides == 10:
        print('A decagon.')
else:
    print('Your input is not in range.')