wave = int(input('Enter a wavelength (nm): '))

if wave in range(380, 450):
	print('Violet')
elif wave in range(450, 495):
	print('Blue')
elif wave in range(495, 570):
	print('Green')
elif wave in range(570, 590):
	print('Yellow')
elif wave in range(590, 620):
	print('Orange')
elif wave in range(620, 750):
	print('Red')
else:
	print('Not in range')