n = int(input())

pr_str = ""
for i in range (1,n):
    if i%2 ==0:
        pr_str += "I love that "
    else:
        pr_str += "I hate that "
if n%2 == 0:
    print (pr_str + "I love it ")
else:
    print (pr_str + "I hate it ")

