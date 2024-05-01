denomination = int(input('Enter a denomination of a banknote: '))

banknotes = {
	1: 'George Washington',
	2: 'Thomas Jefferson',
	5: 'Abraham Lincoln',
	10: 'Alexander Hamilton',
	20: 'Andrew Jackson',
	50: 'Ulysses S. Grant',
	100: 'Benjamin Franklin'
}

if denomination in banknotes:
	print(banknotes[denomination])
elif denomination not in banknotes:
	print("The denomination you've entered does not exist.")