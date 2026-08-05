choice = int(input("1. Celsius to Farenheit\n2.Farenheit to Celsius\nchoice : "))
if choice == 1:
    celsius = float(input("Enter Celsius : "))
    print("Farenheit = ",1.8*celsius+32)
elif choice == 2:
    Farenheit = float(input("Enter Farenheit : "))
    print("Celsius = ",(Farenheit-32)*5/9)
else :
    print("Invalid Choice")
