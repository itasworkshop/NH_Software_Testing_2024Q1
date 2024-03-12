class Student():
    collgName = "NHCK"

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def myIntro(self):
        print("Hey this is ",self.name," i scored ",self.marks," and my colledge is ",self.collgName)


obj = Student("Rajesh",111,79)
obj.myIntro()

obj1 = Student("Tom",222,56)
obj1.myIntro()

def gradeCalculator(stObj):

    if(stObj.marks >= 90 and stObj.marks <=100):
        return "A"
    elif(stObj.marks >= 80 and stObj.marks <90):
        return "B"
    elif (stObj.marks >= 70 and stObj.marks < 80):
        return "C"
    else:
        return "Failed"


print(gradeCalculator(obj))
print(gradeCalculator(obj1))