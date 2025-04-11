LorR = input("").upper()
userinput = input("")
value = "qwertyuiopasdfghjkl;zxcvbnm,./"
newstring = ""
length = len(userinput)

for i in range(length):
    req_index = -1
    for j in range(len(value)): 
        if userinput[i] == value[j]:
            if LorR == 'R':
                req_index = j - 1 
            else:
                req_index = j + 1 
            break

    if 0 <= req_index < len(value):
        newstring += value[req_index]

print(newstring)