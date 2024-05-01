hZ = float(input('Enter a frequency (hZ): '))

notes = {
	261.63: 'C4',
	293.66: 'D4',
	329.63: 'E4',
	349.23: 'F4',
	392.00: 'G4',
	440.00: 'A4',
	-493.88: 'B4'
}

if hZ in notes:
	print(notes[hZ])
elif hZ not in notes:
	print('Your frequency does not correspond to a known note.')