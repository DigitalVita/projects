letter = str(input('Enter a letter: '))

vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

if letter in vowels:
	print('The entered letter is a vowel.')
elif letter == 'y':
	print('Sometimes y is a vowel, and sometimes y is a consonant.')
elif letter in consonants:
	print('The letter is a consonant.')
else:
	print('Not a letter.')