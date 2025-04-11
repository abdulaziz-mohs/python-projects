rating = int(input())

division = ""
if rating < 1200:
    division="Bronze"
elif rating < 1600:
    division="Silver"
elif rating < 2000:
    division="Gold"
else:
    division="Platinum"

print("Your division is: ",division)
