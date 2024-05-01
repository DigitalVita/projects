month = input('Enter a month name: ').lower()

months = {
    'january': '31',
    'february': '28 (29, if in a leap year)',
    'march': '31',
    'april': '30',
    'may': '31',
    'june': '30',
    'july': '31',
    'august': '31',
    'september': '30',
    'october': '31',
    'november': '30',
    'december': '31'
}

if month in months:
    print(f'There are {months[month]} days in {month.capitalize()}.')
else:
    print('Not a month.')