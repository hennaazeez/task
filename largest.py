a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if (a>=b) and (a>=c):
    print(" largest value is:",a)
elif(b>=a) and (b>=c):
    print(" largest value is:",b)
else:
    print(" largest value is:",c)