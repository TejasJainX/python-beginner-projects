print("+--------------------------------------------------------+")
a=float(input("| Enter First Number : "))
b=float(input("| Enter Second Number : "))
c=(input("| Choose Operators (+,-,*,/) :  "))
print("+--------------------------------------------------------+")
if c=="+":
    print("| Result (Addition) :",a+b)
elif c=="-":
    print("| Result (Subtraction) :",a-b)
elif c=="*":
    print("| Result (Multiplication) :",a*b)
elif c=="/":
    print("| Result (Division) :",a/b)
else:
    print("| ERROR: INVALID OPERATOR")
print("+--------------------------------------------------------+")
