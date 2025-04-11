weight=float(input("Please enter your mass in kg: "))
height=float(input("Please enter your height in m: "))
bmi=(weight)/((height)**2)

if bmi<18.5:
    status="under weight"
elif bmi<25:
    status="normal weight"
elif bmi<30:
    status="over weight"
elif bmi<35:
    status="obese"
elif bmi>=35:
    status="clinically obese"

bmi=int(bmi)
print ("Your BMI IS: " + str(bmi) + " ,you are " + status)
