t = int(input('Enter time in seconds: '))

D = HH = MM = SS = 0

while t - 86400 >= 0:
	t -= 86400
	D += 1
while t - 3600 >= 0:
	t -= 3600
	HH +=1
while t - 60 >= 0:
	t -= 60
	MM += 1
SS = t
	
print(f'{D:02}:{HH:02}:{MM:02}:{SS:02}')