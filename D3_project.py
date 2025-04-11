print("Wellcome to the treasure island;")
print("Your measion is to find the treasure.\n")

choise=input("Left or Right: ")
choise=choise.lower()
if (choise=="left"):
    choise=input("Swim or wait: ")
    choise=choise.lower()
    if (choise=="wait"):
       choise=input("Which door Red ,Blue, Yellow: ")
       choise=choise.lower()
       if (choise=="yellow"):
           choise=print("YOU WIN!!! ")
       else:
           print("Game over.")
    else:
           print("Game over.")             

else :
    print("Game over.")    
