class School:
    #school data
    schoolid = "uni21"
    principal = "Orchofo"
    school_name = "GBHS TOOY"
    employeeid = "emp234"
    
#creating the functions in the classes
    def Student(self):
        studentid = "uba21e"
        studentname = "yika"
        studentaddress = "bambili"
        studentclass = "form5"
    def Employee(self):
        employeeid = "emp234"
        post = "classrooms"
        start = "8:00"
        end = "2:30"
    def Courses(self):
        courseid = "mece31"
        coursetitle = "eng drawing"
        courseduration = "2hrs"
        print("courseid " + courseid + "and has a courseduration of " + courseduration )
    def Lecturer(self):
        lecturerid ="chonwa213"
        post = "class5"
        time = "9:00"
#creating the objects
det = School()
print("schoolid " + det.schoolid)
print("principal "+ det.principal)
det.Student()
det.Courses()
det.Lecturer()
print("hello")
