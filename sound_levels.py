dB = int(input('Enter decibels (40 dB - 130 dB): '))

sound_levels = {
    130: 'A jackhammer',
    106: 'A gas lawnmover',
    70: 'An alarm clock',
    40: 'A quiet room'
}

if dB not in sound_levels:
    if dB in range(40, 71):
        print('Your decibles are between a quiet room and an alarm clock.')
    if dB in range(70, 107):
        print('Your decibels are between an alarm clock and a gas lawnmover.')
    if dB in range(106, 131):
        print('Your decibels are betveen a gas lawnmover and a jackhammer.')
elif dB in range(40, 131):
    print(sound_levels[dB])
else:
    print('The decibels you have entered are out of range.')