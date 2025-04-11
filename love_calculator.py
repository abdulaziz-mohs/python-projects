print ("Wellcome to the love callculator!")
name1=input ("What is your name?\n")
name1=name1.lower()
name2=input ("What is his/her name?\n")
name2=name2.lower()
name_total=name1+name2
count1=name_total.count("t")+name_total.count("r")+name_total.count("u")+name_total.count("e")
count1*=10
count2=name_total.count("l")+name_total.count("o")+name_total.count("v")+name_total.count("e")

love_score=count1+count2

if (love_score<10 or love_score>90):
    print(f"Your love score is {love_score}.you go togather like coke and mentos. ")
elif (love_score>40 or love_score<50):
    print(f"Your love score is {love_score}.you are alright togather. ")
else :
    print(f"Your love score is {love_score}")