import random

guess_value = random.randrange(0,50)

counter = 0
limit = 10

while(counter < limit):
    guess = int(input("enter a guess number: "));
    if(guess > guess_value):
        print("the guess value is too high")
    elif(guess < guess_value):
        print("your guess number is too low!!")
    else:
        print("congratulations your guess is correct")

        break

    counter +=1;

else:
    print("you have reached the guess limit\n")
    print("better luck next time\n")
print('enter yes to replay and no to exit!!!')

replay = input("do you want to replay? ")

if(replay == 'yes'):
    counter =0;
    while(counter < limit):
        guess = int(input("enter a guess number: "));
        if(guess > guess_value):
            print("the guess value is too high")
        elif(guess < guess_value):
            print("your guess number is too low!!")
        else:
            print("congratulations your guess is correct")

            break

        counter +=1;

    else:
        print("you have reached the guess limit\n")
        print("better luck next time\n")
else:
    exit