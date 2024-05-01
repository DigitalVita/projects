mag = float(input('Enter an earthquake magnitude (Richter scale): '))

if mag < 2.0:
	print('Micro')
elif mag >= 2.0 and mag < 3.0:
	print('Very minor')
elif mag >= 3.0 and mag < 4.0:
	print('Minor')
elif mag >= 4.0 and mag < 5.0:
	print('Light')
elif mag >= 5.0 and mag < 6.0:
	print('Moderate')
elif mag >= 6.0 and mag < 7.0:
	print('Strong')
elif mag >= 7.0 and mag < 8.0:
	print('Major')
elif mag >= 8.0 and mag < 10.0:
	print('Great')
elif mag >= 10:
	print('Meteoric')