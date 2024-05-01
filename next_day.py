date = input('Enter a date (format: YYYY/MM/DD): ')
yyyy, mm, dd = map(int, date.split('/'))

def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def days(yyyy, mm, dd, day_count):
    if dd < day_count:
        dd += 1
    elif dd == day_count:
        dd = 1
        if mm < 12:
            mm += 1
        else:
            mm = 1
            yyyy += 1
    print(f'Next day: {yyyy}/{mm:02d}/{dd:02d}')

if mm in (1, 3, 5, 7, 8, 10, 12):
    days(yyyy, mm, dd, 31)
elif mm in (4, 6, 9, 11):
    days(yyyy, mm, dd, 30)
elif leap(yyyy):
    days(yyyy, mm, dd, 29)
else:
    days(yyyy, mm, dd, 28)