# student[SID, Name, Gender, Course Name, CGPA]).

SID=int(input("enter the student's student id :"))
Name=input("enter the name of student :")
Gender=input("enter the gender M or F :")
if Gender =="M" or "F" or "m" or "f" :
    Gender=Gender
else:
    Gender="U"
Course_Name=input("enter the course name :")
CGPA=float(input("enter the CGPA :"))
details=[SID,Name,Gender,Course_Name,CGPA]
print('Details of student is :',details)

