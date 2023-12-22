#Multilevel Inheritance

class student:
    def getstudentInfo(self):
        self.name=input("Enter Name:")
        self.rollno=input("Enter Roll NO.")
        self.Class=input("Enter Class:")
class mark(student):
    def getstudentmark(self):
      self.p=int(input("Enter Physice Mark:"))
      self.c=int(input("Enter Chemisry Mark:"))
      self.m=int(input("Enter Maths Mark:"))
class calculate(mark):
    def getdata(self):
        self.Total=self.p+self.c+self.m
        self.Cutoff=self.Total/3
class recorde(calculate):
    def getdisplay(self):
        print("Name:",self.name)
        print("Roll No.:",self.rollno)
        print("class:",self.Class)
        print("Marke in subject:",self.p,self.c,self.m)
        print("Cut Off:",self.Cutoff)
ob=recorde()
ob.getstudentInfo()
ob.getstudentmark()
ob.getdata()
ob.getdisplay()
