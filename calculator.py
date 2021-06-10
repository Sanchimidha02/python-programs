#calculator using python
print("Hey! welcome to my calculator")
print("enter the first number:")
a=int(input())
print("enter the second number:")
b=int(input())
print("which operation you want to use?")
c=input()
if c =="+":
    print("your answer is:", a+b)
elif c =="*":
    print("your answer is:", a*b)
elif c =="/":
    print("your answer is:", a/b)
elif c =="-":
    print("your answer is:", a-b)
elif c =="**":
    print("your answer is:", a**b)
else:
    print("Oops! You did something wrong")
    print("Try again")

    print("\nthankyou for using calculator")





