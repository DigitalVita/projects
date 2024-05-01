Ta = float(input('Air temperature (<=10°C): '))
V = float(input('Wind Speed (>4.8 km/h): '))

WCI = 13.12 + 0.6215*Ta - 11.37*V**0.16 + 0.3965*Ta*V**0.16

print(f'WCI: {int(WCI)}')