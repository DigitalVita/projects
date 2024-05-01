loaves = int(input('How many day old loaves of bread did you purchase?\n>'))

print('Regular price: $3.49\nDiscount for a day old loave of bread: 60%')
print(f'Regular total price: ${3.49 * loaves}')
print(f'Your total price: ${round(loaves - 2.094, 2)}')