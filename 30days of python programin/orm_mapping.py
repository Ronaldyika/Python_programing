#creating my model 
class Person():
    name = input('enter ur name: ')
    email = input('enter ur email: ')
    password = input('enter your password:')

    details = (name,email,password)
    print(details)
    #dic = details.save()
    #print(dic)



    def __str__(self):
        return self.name
    


class userinfo():
    
    user = Person.dic.objects.all()
    print(user)

Person()
userinfo()