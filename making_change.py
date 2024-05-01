cents = float(input('Total cents: '))

pennie = nickel = dime = quarter = 0

while cents > 24:
	cents -= 25
	quarter += 1
	
while cents > 9:
	cents -= 10
	dime += 1
	
while cents > 4:
	cents -= 5
	nickel += 1
	
while cents > 0:
	cents -= 1
	pennie += 1

print('Your change:')	
print(f'Quarters: {quarter}')
print(f'Dimes: {dime}')
print(f'Nickel: {nickel}')
print(f'Pennies: {pennie}')