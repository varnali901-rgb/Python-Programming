a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a+b>c and b+c>a and a+c>b:
    print("TRIANGLE CAN BE CONSTRUCTED")

    if a==b==c:
        print("EQUILATERAL TRIANGLE")
    elif a==b or b==c or a==c:
        print("ISOSCELES TRIANGLE")
    else:
        print("SCALENE TRIANGLE")
else:
    print("TRIANGLE CANNOT BE CONSTRUCTED")
