import math

a = int(input('Enter a value a: '))
b = int(input('Enter a value b: '))
c = int(input('Enter a value c: '))

if a == b == c or a >= b == c:
	print('Provided values yield no real roots')
	exit()

discriminant = math.sqrt(b**2 - 4*a*c)

if discriminant < 0:
	print('Provided values yield no real roots.')
elif discriminant == 0:
	print('Provided values yield one real root.')
	print(f'Root: {(-b + math.sqrt(discriminant)) / (2*a)}')
else:
	print('Provided values yield two real roots.')
	print(f'Root 1: {(-b + math.sqrt(discriminant)) / (2*a)}')
	print(f'Root 2: {(-b - math.sqrt(discriminant)) / (2*a)}')