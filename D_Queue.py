n = int(input())
allnum = input()
splited = allnum.split()
num_array = list(map(int,splited))

num_array.sort()
sum=0
not_disappointed=0
for i in range(n):
    if(num_array[i] >= sum):
        not_disappointed+=1
    sum+=num_array[i]
print (not_disappointed)