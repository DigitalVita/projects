m_and_d = input('Enter a month and a day (e.g. June 21): ').capitalize()

seasons = {
	'March 20' : 'Spring',
	'June 21' : 'Summer',
	'September 22' : 'Fall',
	'December 21' : 'Winter'
}

print(seasons[m_and_d])