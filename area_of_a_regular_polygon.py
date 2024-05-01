import math

s = int(input('Length of a side: '))
n = int( input('Number of sides: '))

a = (n * s**2) / (4 * math.tan(math.pi/n))

print(f'Area: {a}')