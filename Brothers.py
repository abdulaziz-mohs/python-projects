n ,k = map(int , input("").split())
a = list(map(int , input("").split()))
a.append(0)

nd=0

for i in range (n):
    nd=i+1
    if a[i] <= 8:
        k-=a[i]
    else:
        k-=8
        a[i+1]+= a[i]-8
    
    if k<=0:
        print (nd)
        break


if(k>0):
    print(-1)   


