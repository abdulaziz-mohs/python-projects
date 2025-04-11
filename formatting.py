#see the use and difference of each in this example
a=15.23899899999999
print(round(a,4))   #it rounds to 4 digit and do not print the right most zero's which don't have nonzero after it
                    #eg: print(round(a,4)) will give 15.239 not 15.2390(this 0 will be left by the round function) 

print("%.7f"%a)     # it both rounds and formatts using 7
                    # it will print 15.2389990(round it at the 7th digit and also formatted it to have 7 digit by adding one 0)

print("{:.7f}".format(a)) #The same as the above.

print("%.7f"% round(a,2))  # it rounds using 2 and formatt it using 7(by adding 0's untill it have 7 decimal place.)
                           # it will print 15.2400000(it round it at 2nd digit and add 0's until it have 7 decimal place.)

print("{:.7f}".format(round(a,2)))  #The same as the above.

