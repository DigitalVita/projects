meal_cost = float(input('Enter a price of your meal: '))

w_tax = meal_cost * 0.1  # 10% tax
w_tip = meal_cost * 0.18 # 18% tax

print(f'Tax and tip: {round((w_tax + w_tip), 2)}')
print(f'Ground total: {round((meal_cost + w_tax + w_tip), 2)}')