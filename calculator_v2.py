print("+--------------------------------------------------------+")
a=float(input("| Enter First Digit : "))
b=float(input("| Enter Second Digit : "))
c=float(input("| Enter Third Digit : "))
d=input("| Choose First Operator(+,-,*,/) : ")
e=input("| Choose Second Operator(+,-,*,/) : ")
print("+--------------------------------------------------------+")
if d=="+" and e=="+":
    print("| Result :",a+b+c)
elif d=="+" and e=="-":
    print("| Result :",a+b-c)
elif d=="+" and e=="*":
    print("| Result :",a+b*c)
elif d=="+" and e=="/":
    print("| Result :",a+b/c)
elif d=="-" and e=="+":
    print("| Result :",a-b+c)
elif d=="-" and e=="-":
    print("| Result :",a-b-c)
elif d=="-" and e=="*":
    print("| Result :",a-b*c)
elif d=="-" and e=="/":
    print("| Result :",a-b/c)
elif d=="*" and e=="+":
    print("| Result :",a*b+c)
elif d=="*" and e=="-":
    print("| Result :",a*b-c)
elif d=="*" and e=="*":
    print("| Result :",a*b*c)
elif d=="*" and e=="/":
    print("| Result :",a*b/c)
elif d=="/" and e=="+":
    print("| Result :",a/b+c)
elif d=="/" and e=="-":
    print("| Result :",a/b-c)
elif d=="/" and e=="*":
    print("| Result :",a/b*c)
elif d=="/" and e=="/":
    print("| Result :",a/b/c)
else:
    print("| ERROR: INVALID OPERATOR")
print("| Thank You For Using Our Calculator!")
print("+--------------------------------------------------------+")
