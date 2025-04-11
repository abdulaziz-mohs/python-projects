a = input("")
b = input("")

sumwithzero = int(a) + int(b)
azero=""
bzero=""

for i in range(len(a)):
    if a[i] != '0':
        azero+=a[i]

for i in range(len(b)):
    if b[i] != '0':
        bzero+=b[i]

sumzero=0
for i in range(len(sumwithzero)):
    if sumwithzero[i] != '0':
        sumzero+=b[i]

if (int(azero) + int(bzero)) == sumzero:
    print("YES")
else:
    print("NO")