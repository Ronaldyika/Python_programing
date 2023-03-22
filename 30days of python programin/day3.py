#string formating . understanding the f-string

name = input("enter a name: ");
year_of_birth = int(input("enter your year of birth: "));
current_year = int(input("enter the present year: "));

age = (current_year - year_of_birth);

print(f'my name is {name} and i was born in {year_of_birth}, so that makes me {age} years old!!!')