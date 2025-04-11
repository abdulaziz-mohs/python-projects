t = int (input())
for i in range(t):
    n = int(input())
    allnum = input()
    splited = allnum.split()
    num_array = list(map(int,splited))

    print(max(num_array)-min(num_array))