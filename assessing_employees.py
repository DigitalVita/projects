rating = float(input('Enter a rating: '))

ratings = {
	0.0 : 'Unacceptable performance',
	0.4 : 'Acceptable performance',
	0.6 : 'Meritorious performance'
}

if rating in ratings:
	print(ratings[rating])
	print(f'Raise: ${rating*2400.00}')
elif rating > 0.6:
	print('Meritorious performance')
	print(f'Raise: ${rating*2400.00}')