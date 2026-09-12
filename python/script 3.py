a=int (input("enter number 1:"))
b=int (input("enter number 2:"))
c=int (input("enter number 3:"))
if (a>=b) and (a>=c):
    largest_number=a
elif (b>=a) and (b>=c):
    largest_number=b
else:
    largest_number=c
print("greatest value among given three numbers is:",largest_number)