print('Hello')

choice = ''
less_than_L = 0
more_than_L = 0

while choice != 'n':
    quantity = int(input('How many containers would you like to submit?\n>'))
    volume = float((input('What is the volume of your container(s)?\n>')))
    if volume <= 1:
        less_than_L += quantity
    elif volume > 1:
        more_than_L += quantity
    choice = input('Would you like to submit more containers?\n(y)es, (n)o\n>')

less_than_L *= 0.10
more_than_L *= 0.25

print(f'Your total refund is: ${less_than_L + more_than_L}')