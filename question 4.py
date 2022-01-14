marks_list=list()
for i in range(1,6):
    marks=int(input(f"enter marks of {i} student :"))
    marks_list.append(marks)
print(marks_list)
marks_list.sort()
print("marks of 5 students in sorted manner",marks_list)
