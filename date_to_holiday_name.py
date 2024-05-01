month_and_day = input('Enter a month and a day (ex. January 1): ')

holidays = {
	'January 1': "New year's day",
	'July 1': 'Canada day',
	'December 25': 'Christmas day'
}

if month_and_day in holidays:
	print(holidays[month_and_day])
elif month_and_day not in holidays:
	print('The entered month and day do not correspond to a fixed-date holiday.')