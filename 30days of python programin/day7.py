#the join function

authors = ['peter', 'paul','john']
authors = ",".join(authors);

print(f'the people who worked on this project are, {authors}');


games = ['ludo','dice','paper','scisores']

print(f'the games i love are {",".join(games)}')

numbers = range(0,100)
odd_numbers = []
even_numbers = []

for number in numbers:
    if(number%2 ==0):
        even_numbers.append(number);
    else:
        odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)