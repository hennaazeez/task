n=int(input("enter the no :"))
reverse=0
while n>0:
    remainder=n % 10
    reverse=(reverse*10)+remainder
    n=n//10
print("reversed no is:",str(reverse))