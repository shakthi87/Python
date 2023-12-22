#Hybrid

#hybrid

class student:
    def getstudentinfo(self):
        self.name=input("Enter Name:")
        self.dob=input("Enter Date of Birth:")
        self.age=int(input("Enter Age:"))
class Department(student):
    def getdepartmentneed(self):
        self.d1=input("Enter First choice Department:")
        self.d2=input("Enter Second choice Department:")
class education(Department):
    def geteducationinfo(self):
        self.s=input("Enter School Name:")
        self.tm=int(input("Enter Total Mark:"))
class result(education):
    def display(self):
        print("---Verification---")
        print("Name:",self.name)
        print("Date of Birth:",self.dob)
        print('School Name:',self.s)
        print('Total Mark:',self.tm)
        print('First choice Department',self.d1)
        print('Second choice Department',self.d2)

ob=result()
ob.getstudentinfo()
ob.geteducationinfo()
ob.getdepartmentneed()
ob.display()
