a=int (input("enter number 1:"))
b=int (input("enter number 2:"))
c=input("enter your choice:")
if c=='+':
    print("sum of 2 numbers",a+b)
elif c=='-':
    print("difference of 2 numbers",a-b)
elif c=='*':
    print("product of 2 numbers",a*b)
elif c=='/':
    print("quotient of 2 numbers",a/b)
else:
    print("wrong choice")