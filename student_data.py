class Student:
    def __init__(self, fname, lname, dob, jobrole):
        self.firstname = fname
        self.lastname = lname
        self.dateofbirth = dob
        self.jrole = jobrole

    def printname(self):
        print(self.firstname, self.lastname)

    def date_of_birth(self):
        print(self.dateofbirth)

    def jrole(self):
        print(self.jrole)


n = Student("Sohaib", "Sohail", "03/07/1998", "DevOps Engineer")
Student.printname("Sohaib", "Sohail"), Student.date_of_birth("03/07/1998"), Student.jrole("Dev Ops Engineer")

