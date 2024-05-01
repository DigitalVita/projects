Hz = float(input('Enter a frequency (Hz): '))

if Hz < 3*10**9:
	print('Radio waves')
elif Hz >= 3*10**9 and Hz < 3*10**1:
	print('Microwaves')
elif Hz >= 3*10**12 and Hz < 4.3*10**14:
	print('Infrared light')
elif Hz >= 4.3*10**14 and Hz < 7.5*10**14:
	print('Visible light')
elif Hz >= 7.5*10**14 and Hz < 3*10**17:
	print('Ultraviolet light')
elif Hz >= (3*10**17 and Hz < 3*10**19):
	print('X-rays')
elif Hz >= 3*10**19:
	print('Gamma rays')
else:
	print('Not in range')