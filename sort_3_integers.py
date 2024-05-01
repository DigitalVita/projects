i1 = int(input('Enter the 1st integer: '))
i2 = int(input('Enter the 2nd integer: '))
i3 = int(input('Enter the 3d integer: '))

received_integers = (i1, i2, i3)

print(f'Smallest value: {min(received_integers)}')
print(f'Middle value: {(i1+i2+i3) - min(received_integers) - max(received_integers)}')
print(f'Largest value: {max(received_integers)}')