#basic game by machine
for number in range(1,101):
    if number % 3 ==0:
        if number % 5 == 0:
            print("fizz buzz")
        else:
            print("fizz")
    if number % 5 == 0:
        print("buzz")
    else:
        print(number)

#fizz buzz game taking numbers from user

limit = int(input("enter your limit: "))
count = 0;
Range = int(input("enter  a range for your game: "))
while (limit >= count):
    number = int(input("enter a number: "));
    if(number <= Range):
        if (number % 5) == 0:
            if(number % 3) == 0:
                print("fizz buzz");
            else:
                print("buzz")
        elif number % 3 == 0:
            print("fizz") 
        else:
            print(number)

    count += 1;

else:
    print("the limit is exceeded guy!!!!")


