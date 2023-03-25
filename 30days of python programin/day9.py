#enumerations

list = ['cars', 'friuts', 'people']
counter = 1;

for counter, name in enumerate(list, start=1):
    print(f'{counter}.{name}')