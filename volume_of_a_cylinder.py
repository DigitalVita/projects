import math

r = float(input(f'Radius of a cylinder: '))
h = float(input(f'Height of a cylinder: '))

A = math.pi * r**2
volume = h * A

print(f'Volume: {round(volume, 1)}')