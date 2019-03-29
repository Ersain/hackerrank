import math
def gradingStudents(grades):
    return [math.ceil(i/5)*5 if math.ceil(i/5)*5-i<3 and i>=38 else i for i in grades]
