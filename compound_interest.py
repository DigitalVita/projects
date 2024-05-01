deposit = float(input('Your deposit: '))

y1 = deposit * .04 + deposit
y2 = y1 * .04 + y1
y3 = y2 * .04 + y2

print(f'First year: {round(y1, 2)}')
print(f'Second year: {round(y2, 2)}')
print(f'Third year: {round(y3, 2)}')