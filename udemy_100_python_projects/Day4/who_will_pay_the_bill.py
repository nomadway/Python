import random

version 1 (difficult one)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_person = random.randint(0, number_of_names -1)
person_who_will_pay = names[random_person]
print(f'{person_who_will_pay} is going to pay the bill today.')

#version 2 (easy one)

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# person_who_will_pay = random.choice(names)
# print(f'{person_who_will_pay} will pay the bill.')


#version 3

# names = ['YUri', 'Mark', 'Jack']
# person_who_will_pay = random.choice(names)
# print(f'{person_who_will_pay} will pay the bill.')
