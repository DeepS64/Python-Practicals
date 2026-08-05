a = int(input("Enter Num1 : "))
b = int(input("Enter Num2 : "))
c = int(input("Enter Num3 : "))

if a>b :
    if a>c:
        print(a, " is largest")
    else:
        print(c, " is largest")
else:
    if b>c:
        print(b, " is largest")
    else:
        print(c, " is largest")