import string


class Men:
    def __init__(self):
        name = input("enter name: ")
        age = int(input("enter age: "))
        color = input("describe your complexion: ")
        print(name)
        print(age)
        print(color)
        
    def display(self):
        print(" the above are some attrubutes of a man")
        
man1 = Men()
man1.display()
man2 = Men()
man2.display()

