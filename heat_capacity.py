m = float(input('Enter a mass of water: '))
dT = int(input('Enter a temperature change: '))

q = m * 4.186 * dT
JtokWh = q * 2.777778 * 10**-7
cost = JtokWh * 8.9

print(f'Total energy: {q} J.')
print(f'kWh: {JtokWh} kWh, cost: {cost} cents.')