DoB = input('Enter your date of birth(e.g. December 22): ').capitalize()
DoB = DoB.split(' ')
month = DoB[0]
day = int(DoB[1])

if month == 'December' and day in range(22, 32) or month == 'January' and day in range(1, 20):
	print('Capricorn')
elif month == 'January' and day in range(20, 32) or month == 'February' and day in range(1, 19):
	print('Aquarius')
elif month == 'February' and day in range(19, 30) or month == 'March' and day in range(1, 21):
	print('Pisces')
elif month == 'March' and day in range(21, 32) or month == 'April' and day in range(1, 20):
	print('Aries')
elif month == 'April' and day in range(20, 31) or month == 'May' and day in range(1, 21):
	print('Taurus')
elif month == 'May' and day in range(21, 32) or month == 'June' and day in range(1, 21):
	print('Gemini')
elif month == 'June' and day in range(21, 31) or month == 'July' and day in range(1, 23):
	print('Cancer')
elif month == 'July' and day in range(23, 32) or month == 'August' and day in range(1, 23):
	print('Leo')
elif month == 'August' and day in range(23, 32) or month == 'September' and day in range(1, 23):
	print('Virgo')
elif month == 'September' and day in range(23, 31) or month == 'October' and day in range(1, 23):
	print('Libra')
elif month == 'October' and day in range(23, 32) or month == 'November' and day in range(1, 22):
	print('Scorpio')
elif month == 'November' and day in range(22, 31) or month == 'December' and day in range(1, 22):
	print('Sagittarius')