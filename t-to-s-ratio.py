import easygui as eg

try:
    # number_entered = eg.integerbox("Enter number of students per class (inbetween 10 and 30)")
    # if 10 < number_entered < 30:

    teacher_number = eg.integerbox("Number of teachers")
    student_per_class = eg.integerbox("Number of students per class")
    class_number = eg.integerbox("Number of classes")
    total_students = class_number * student_per_class
    teachers_needed = f"{(total_students / 30):,.0f}"
    print(teacher_number)
except:
    print("Error")
