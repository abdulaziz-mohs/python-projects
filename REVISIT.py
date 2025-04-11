import math

num = int(input("Enter an integer number: "))
n = len(str(num))
a=n
x=int(num)
sums=int(0)
y=int(0)
total =""
for _ in range (0,a+1):
    
    if n==0:
        total = (f"{total} = {sums}")
        print(total)
    else :
        n-=1
        y=math.floor(x/pow(10,n))
        sums = sums + y
        x = x-(y * 10**n)
        if n> 0:
            total = (f"{total} {y} +")
        else:
            total = (f"{total} {y}")


        


    