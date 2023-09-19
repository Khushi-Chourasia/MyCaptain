a=0
b=1
c=a+b
n=int(input("Enter the number upto which you require Fibonacci series for:"))
print("Fibonacci Series:" ,a,"\n",b)
for i in range(3,n):
    print(c)
    a=b
    b=c
    c=a+b

