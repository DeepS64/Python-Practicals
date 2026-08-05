def isPalindrome(a):
    f = str(a)
    if f == f[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
        
a = input("Enter a string")
isPalindrome(a)