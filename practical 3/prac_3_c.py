a = int(input("Enter a num1 : "))
b = int(input("Enter a num2 : "))
for i in range(a,b+1):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)