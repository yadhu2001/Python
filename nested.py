a=input("Do you want to continue? Y/N")
if a=='Y' or a=='y':
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))
    z=int(input("Enter third number"))
    if x==y==z:
        print("three values are equal")
    elif x>=y and x>=z:
        print(x,"is greater")
    elif y>=x and y>=z :
        print(y,"is greater")
    else:
        print(z,"is greater")
else:
    print("program terminated")


