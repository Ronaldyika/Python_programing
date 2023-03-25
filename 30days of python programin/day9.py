#enumerations

list = ['cars', 'friuts', 'people']
counter = 1;

for counter, name in enumerate(list, start=1):
    print(f'{counter}.{name}')

pets = ['dogs','cats','ducks','rabits']

owner = ['men','women','family','farmer']


belongs_to = zip(owner,pets)
print((belongs_to))