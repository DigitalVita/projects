n = input('Enter a note: ').upper()

notes = {
'C4': 261.63,
'D4': 293.66,
'E4': 329.63,
'F4': 349.23,
'G4': 392.00,
'A4': 440.00,
'B4': 493.88
}

if n not in notes:
    n = n.replace('C', '')
    n = int(n)
    hZ = (261.63) / 2**(4-n)
    print(f'The hZ for the entered note is {hZ} hZ.')
elif n in notes:
    print(f'The hZ for the entered note is {notes[n]} hZ.')