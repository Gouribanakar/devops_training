student = {"kush":100, "gouri":85}

#Add a new student and grade.
name = input("enter the name:")
grade = int(input("enter the grade:"))

student[name]=grade
print(student)

#Update an existing student's grade.
name = input("enter the students name:")

if name in student:
    print(name, "already exists")
    grade = int(input("enter the grade:"))
    student[name]=grade
    print(student)

else:
    print(name," not found")


#Print all student grades.
for x in student.values():
    print(x)