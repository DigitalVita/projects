value = int(input('Enter a collection of values, enter a 0 if you are finished entering your values:\n>'))

if value > 0:
	values = []
	while value != 0 :
		values.append(value)
		value = int(input('>'))
elif value <= 0:
	print('You will need to input at least one positive integer.')
	exit()

print(f'Average {sum(values) / len(values)}')