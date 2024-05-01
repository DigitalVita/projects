P = int(input('Enter a pressure (Pascals): '))
V = float(input('Enter a volume (L): '))
T = float(input('Enter a temperature (K): '))

n = (P*V) / (8.314*T)

print(f'Amount of gas: {n} mol.')