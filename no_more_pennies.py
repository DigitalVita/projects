prices = input('Enter prices in dollars and cents. Press "Space" when you are done.\n>')

list_of_prices = []
while prices != ' ':
    list_of_prices.append(float(prices))
    prices = input('Enter prices in dollars and cents. Press "Space" when you are done.\n>')

total = sum(list_of_prices) * 100

remainder = total % 5

if remainder < 2.5:
    calc = total - remainder
else:
    calc = total + (5 - remainder)

print(f'Total: ${total / 100}')
print(f'To pay: ${calc / 100}')