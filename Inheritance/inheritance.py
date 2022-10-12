#single Inheritance 
class Parent:
    def Pdisplay(self):
        print("this is the parent class ")
class Child(Parent):
    def Childshow(self):
        print("this is the child class \n")

#creating the instances of the class
show = Child()
show.Pdisplay()
show.Childshow()

#multilevel inheritance
#we are going to use 3 classes here which will act as our 
#grandparent , parent and child class 
class Grandparent:
    def Gparent(self):
        print("i have arms")
        
class Parent(Grandparent):
    def Parent(self):
        print("i have a head")
        
class Child(Parent):
    def Child(self):
        print("i go to school")
        
        
#creating the objects(instances of the class)

detail = Child()
detail.Gparent()
detail.Parent()
detail.Child()

    