"""For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”)."""



side1=int(input("enter the 1st side of triangle :"))
side2=int(input("enter the 2nd side of triangle :"))
side3=int(input("enter the 3rd side of triangle :"))

if side1<side2+side3:
    if side2<side1+side3:
        if side3<side1+side2:
            print("yes triangle is possible")
        else:
            print("NO triangle is not possible")
    else:
        print("NO triangle is not possible")
else:
    print("NO triangle is not possible")
