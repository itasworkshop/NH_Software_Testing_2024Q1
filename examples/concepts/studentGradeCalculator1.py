
def gradeCalculator(marks):

    if(marks >= 90 and marks <=100):
        return "A"
    elif(marks >= 80 and marks <90):
        return "B"
    elif (marks >= 70 and marks < 80):
        return "C"
    else:
        return "Failed"


stmarks = 76
print(gradeCalculator(stmarks))
