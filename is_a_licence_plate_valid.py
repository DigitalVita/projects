plate = input('Enter a license plate number: ')

if len(plate) == 6:
    if plate[:3].isalpha() and plate[3:].isdigit() and plate.isupper():
        print('The characters are valid for an older style plate.')
    elif plate.islower():
        print('Use capital letters.')
    else:
        print('Not a valid input.')
elif len(plate) == 7:
    if plate[:4].isdigit() and plate [4:].isalpha() and plate.isupper():
        print('The characters are valid for a newer style plate.')
    elif plate.islower():
        print('Use capital letters.')
    else:
        print('Not a valid input.')
else:
    print('Not a valid input.')