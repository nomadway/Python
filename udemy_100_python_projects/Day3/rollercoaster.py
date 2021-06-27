print('Wellcome to the AWESOME rollercoaster!')
height = float(input('How tall are you in cm?:'))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster.')

    age = int(input('How old are you? '))
    if age < 12:
        bill = 5
        print('Child ticket is $5')
    elif age <= 18:
        bill = 10
        print('Youth ticket is $10')
    
    elif age >= 45 and age <=55:
        bill = 0
        print('Your ticket is $0.')
    else:
        bill = 20
        print('Adult ticket is $20')

    want_photo = input('Do you want a photo? Y or N: ')    #photo costs $3
    if want_photo == 'Y':
        bill += 3   #same as bill = bill + 3
    print(f'Your final bill is ${bill}')


else:
    print('YOu cannot ride the rollercoaster.')