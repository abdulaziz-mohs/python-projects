from collections import Counter

n = int(input())
cards = [int(input()) for _ in range(n)]

counts = Counter(cards)

if len(counts) < 2:
    print("NO")
else:
    unique_elements = list(counts.keys())
    found_fair = False
    ashe_choice = -1
    jose_choice = -1

    for i in range(len(unique_elements)):
        for j in range(i + 1, len(unique_elements)):
            val1 = unique_elements[i]
            val2 = unique_elements[j]

            count1 = counts[val1]
            count2 = counts[val2]

            if count1 == n // 2 and count2 == n // 2 and val1 != val2:
                found_fair = True
                ashe_choice = val1
                jose_choice = val2
                break 
        if found_fair:
            break  

    if found_fair:
        print("YES")
        print(ashe_choice, jose_choice)
    else:
        print("NO")