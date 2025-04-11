print ("Welcome to python piza deliveries!")
size=input ("What size of pizza do you want? 'S','M','L': ")
add_peperroni=input ("Do you want peperroni? 'Y'/'N': ")
extra_cheese=input ("Do you want extra cheese? 'Y'/'N': ")
bill=0
if size=="S":
    bill=15
elif size=="M":
    bill=20
else:
    bill=25

if add_peperroni=="Y":
    if size=="S":
       bill+=2
    else:
       bill+=3

if extra_cheese=="Y":
   bill+=1

print(f"Your final bill is {bill}")              