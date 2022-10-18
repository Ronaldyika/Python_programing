import string
from xml.etree.ElementPath import prepare_parent


class Men:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age 
        self.color = color
        
    def display(self):
        print(" the above are some attrubutes of a man")
class Animals:
    def Dog(self):
        print("the info below prints some xtics of dogs: \n ")
        Description_teath = "sharp pointed teeths"
        body = "has a backbone and tail"
        color  = "it has random colors"
        life_span = "can live up to 10yrs"
        print(Description_teath)
        print(body)
        print(color)
        print(life_span ,"\n")
    def Man(self):
        #some features of a man
        print("\nthe info below are some xtics of a man \n")
        Man_name = "has a name"
        age = "always have a particular age and they vary"
        gender = "Male / Female"
        status = "personal"
        print(Man_name)
        print(age)
        print(gender)
        print(status,"\n")
        
            
#choosing the output you want

detail = Men("green",12,"fair")
anim = Animals()
print("\nenter 1 for defining some xtics of man,2 to see the charaters of a dog\n")
print("enter 3 to display some features of a man \n")
choice = int(input("please enter the number of what you want: "))  
#the choice displays the option you want to be displayed onto a user

if choice == 1:
    detail.display()
    name = input("enter name: ")
    age = int(input("enter age: "))
    color = input("describe your complexion: \n")
    print("my name is " + name )
    print( "i am " + str(age) + " years old today")
    print(color ,"\n")
elif choice == 2:
    anim.Dog()
elif choice == 3:
    anim.Man()
else:
    print("sorry out of scope")
      
   
        

