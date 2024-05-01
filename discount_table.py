prices = [4.59, 9.95, 14.95, 19.95, 24.95]

for i in prices:
	print('××××××××××××××××××××××')
	print(f'Original price: ${i}')
	print(f'Discount: ${round((i*60/100), 2)}')
	print(f'New price: ${round(i - (i*60/100), 2)}')
	print('××××××××××××××××××××××')