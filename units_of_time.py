d = int(input('Days: '))
h = int(input('Hours: '))
m = int(input('Minutes: '))
s = int(input('Seconds: '))

d *= 86400
h *= 3600
m *= 60

print(f'Total: {d+h+m+s} s.')