#creating a simple dictionary with basic info about a student
from lockfile import LockTimeout


Details = {"f_name": "Sahla", "l_name": "Sandrine", "DOB":"2012"}
Details["Class"] = "form2"
print(Details,"\n")
#editing contents of a dictionaary
Details["f_name"] = "Ronald"
Details["l_name"] = "Yika"
print(Details)
#deleting contents from a dictionary

del Details["DOB"]
print(Details)


#dictionary in dictionaries

Students_info = {
    "Student_one": {
        "f_name" : "Ronald",
        "l_name" : "Yika",
        "location" : "Bambili",
        "Age" : 21
    },
    "Student_two": {
        "f_name" : "chantal",
        "l_name" : "limnyuy",
        "location" : "baffusam",
        "Age" : 23
    },
    "Student_three": {
    "f_name" : "Nyuyfoni",
    "l_name" : "Juliene",
    "location" : "baffusam",
    "Age" : 17
},
    "Student_four": {
    "f_name" : "fai",
    "l_name" : "Sonia",
    "location" : "baleng",
    "Age" : 16
}
}


#looping through a dictionary can be done as shown below
for student, detail in Students_info.items():
    print("\nstudent: ", student)
    full_name = detail["f_name"] +" "+ detail["l_name"]
    print("Name: " + full_name)
    location = detail["location"]
    print("location: ", location)
    age = detail["Age"]
    print("Age: ", age ,"\n")
    
    
     #printing or displaying only the values
     
     
for detail in Students_info.values():
    name = detail["f_name"] + " " + detail["l_name"]
    print("Name: ", name)
    location = detail["location"]
    age = detail["Age"]
    print("I am located at ", location)
    print("I am ", age,"years old\n")
    
    
