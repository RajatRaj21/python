#Write a python program to find the greatest of three numbers entered by the user.

no1=int(input("enter any no :"))
no2=int(input("enter any no :"))
no3=int(input("enter any no :"))

if no1>no2:
        if no1>no3 :
            print("The gratest no is ",no1)
        else:
            print("The gratest no is ",no3)
else:
    if no2>no3:
        print("The gratest no is ",no2)
    else:
        print("The gratest no is ",no3)
