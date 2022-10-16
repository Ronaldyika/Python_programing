#implementing python lists
#creating an empty list

from cmath import sqrt


Names = []

#basic operations with list include
#adding, removing, looping and updating items in a list

#adding items
#using the append method

Names.append("Ronald")
Names.append("Catherine")
print(Names)
#using the insert methon

Names.insert(0,"Juliene")
Names.insert(-1,"Felix")
Names.insert(-1,"Paul")
Names.insert(-1,"Peter")
Names.insert(-1,"James")
print(Names)


        #removing elements 
#del Names(1)
#print(Names)
Deleted = Names.pop(1)
Deleted_Names = []
Deleted_Names.append(Deleted)
print(Deleted_Names)
Names.remove("Peter")#the remove is used when the index of the item
#is uknown
print(Names)

#changing value of item in list(Felix will be elliminated 
# and replaced with Telma )

Names[1] = "Telma"
print(Names)

#organising the list in alphabetic or reverse order

Names.sort()

#printing in alphabetic order
print(Names)

#printing in reverse order

Names.reverse()
print(Names)

#looping through a list

for name in Names:
    print(name + "is an example of a noun \n")


#some operations with list numbers

numbers = list(range(2,22))
print(max(numbers))#returns 21 since the highest number is 21
print(min(numbers))#returns 2
print(sum(numbers))#sum the individual items in the list and displays the ans
#for number in numbers:
    #print(sqrt(number))