human = int(input('How old are you?\n>'))

if human > 0:
    dog = (human-2) * 4 + 21
    print(f'Your age in dog years: {dog} years.')
else:
    print('Enter a positive integer.')