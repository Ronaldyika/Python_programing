#sets . a set is a collection of diff elements

from readline import set_pre_input_hook


set_odd_num = {1,3,5,5,7,6}
print(set_odd_num)#printing the set, 4 will be displayed only 
#once since sets elliminates duplicates
 
 
 #adding ellements to a set
 
set_odd_num.add(9)
set_odd_num.add(11)
set_odd_num.add(7)
print(set_odd_num)


set_even_num = {2,4,6,8,10}
set_even_num.add(2)

print(set_even_num)

set_odd_num.update(set_even_num)
print(set_odd_num)


print(len(set_odd_num)) #used to print the length of the set

#removing ellements from the set

set_odd_num.remove(11)#returns an error if the element is not found in the set
set_odd_num.discard(11)#runs the code even if the element is not found in the set
set_odd_num.pop()#pop in sets removes the first number in the set
print(set_odd_num)
#the clear function is used to delete all the items in the list.

set = {2,4,6,7}
set.clear()
print(set)#returns an empty set


#some set operations

print(set_odd_num.isdisjoint(set_even_num),"\n")#prints false since the set is not disjoint



print(set_odd_num.issuperset(set_even_num))#returns true since its a superset of the even numbers


print(set_even_num.union(set_odd_num),"\n")


print(set_odd_num.difference(set_even_num),"\n")




                                                #lanbda functions
                                                
# syntax : (lambda arg: expression)
print("working with lamda functions \n")
product = lambda x,y: x*y
print(product(3,6))


#parameters can still be passed directly to the lambda function

sum = (lambda x=20,y=2, z =40: x+y+z)
print(sum)

add = lambda x,y=10,z=12: x+y+z
print(add(3))

function = (lambda x,function1: function1/x)

print(function(2,function1 = (lambda a =3,b = 4,c = 6: pow(b,2)-4*a*c)))
