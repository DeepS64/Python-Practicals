def Sinterest(p,r,t):
    return p*r*t/100
    
p = int(input("Enter Principle amount : "))
r = float(input("Enter Rate of Interest : "))
t = float(input("Enter Number of years : "))
print("Interest is : ", Sinterest(p,r,t))