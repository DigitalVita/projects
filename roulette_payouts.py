import random

spin = random.randint(0, 37)

red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)

def color(spin):
	if spin in red:
		return 'Red'
	elif spin in black:
		return 'Black'

def oddity(spin):
	if spin % 2 == 0:
		return 'Even'
	elif spin % 2 != 0:
		return 'Odd'
		
def from_to(spin):
	if spin in range(1, 19):
		return '1 to 18'
	elif spin in range(19, 37):
		return '19 to 36'

if spin == 37:
	print('The spin resulted in 00...')
	print('Pay 00')
elif spin in range(0, 36):
	print(f'The spin resulted in {spin}')
	print(f'Pay {spin}')
	print(f'Pay {color(spin)}')
	print(f'Pay {oddity(spin)}')
	print(f'Pay {from_to(spin)}')