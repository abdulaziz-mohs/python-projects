n = int(input())
coin_values_str = input()
coin_values_list_str = coin_values_str.split()
coin_values = [int(value) for value in coin_values_list_str]

coin_values.sort(reverse=True)
total=0
for number in coin_values:
    total += number
avg = total//2
stricthalf=0
i=0
while stricthalf <=avg:
    stricthalf += coin_values[i]
    i+=1

print (i)