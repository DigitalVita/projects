air = int(input('Enter a number of minutes that were used this month: '))
txt = int(input('Enter a number of text messages that were used this month: '))

if air <= 50 and txt <= 50:
    print('Base charge: $15')
    print('Additional cost: $0')
    print('Additional charge (to support 911): $0.44')
    print('Sales tax: 5%')
    print(f'Total: ${((15 + 0.44) * 0.05) + (15 + 0.44)}')
elif air > 50 and txt <= 50:
    print('Base charge: $15')
    print(f'Additional cost: ${(air-50) * 0.25}')
    print('Additional charge (to support 911): $0.44')
    print('Sales tax: 5%')
    print(f'Total: ${((15 + (air-50) * 0.25 + 0.44) * 0.05) + (15 + (air-50) * 0.25 + 0.44)}')
elif air <= 50 and txt > 50:
    print('Base charge: $15')
    print(f'Additional cost: {(txt-50) * 0.15}')
    print('Additional charge (to support 911: $0.44)')
    print('Sales tax: 5%')
    print(f'Total: ${((15 + (txt-50) * 0.15 + 0.44) * 0.05) + (15 + (txt-50) * 0.15 + 0.44)}')
elif air > 50 and txt > 50:
    print('Base charge: $15')
    print(f'Additional cost: ${(air-50) * 0.25 + (txt-50) * 0.15}')
    print('Additional charge (to support 911: $0.44)')
    print('Sales tax: 5%')
    print(f'Total: ${((15 + (air-50) * 0.25 + (txt-50) * 0.15 + 0.44) * 0.05) + (15 + (air-50) * 0.25 + (txt-50) * 0.15 + 0.44)}')