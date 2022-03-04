print("EXAM GRADE CALCULATOR")
midterm1 = float(input("midterm1:"))
midterm2 = float(input("midterm2:"))
final = float(input("final:"))
exam_grade = (midterm1 * (3/10)) + (midterm2 * (3/10)) + (final * (2/5))
if exam_grade >= 90 and exam_grade <= 100:
    print("exam grade: {} AA".format(exam_grade))
elif exam_grade < 90 and exam_grade >= 85:
    print("exam grade: {} AB".format(exam_grade))
elif exam_grade < 85 and exam_grade >= 80:
    print("exam grade: {} BB".format(exam_grade))
elif exam_grade < 80 and exam_grade >= 75:
    print("exam grade: {} CB".format(exam_grade))
elif exam_grade < 75 and exam_grade >= 70:
    print("exam grade: {} CC".format(exam_grade))
elif exam_grade < 70 and exam_grade >= 65:
    print("exam grade: {} DC".format(exam_grade))
elif exam_grade < 65 and exam_grade >= 60:
    print("exam grade: {} DD".format(exam_grade))
elif exam_grade < 60 and exam_grade >= 55:
    print("exam grade: {} FD".format(exam_grade))
elif exam_grade < 55:
    print("exam grade: {} FF".format(exam_grade))
else:
    print("wrong input")
