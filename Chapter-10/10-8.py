import random

def birthday_paradox(number_of_students,number_of_trials):
    count = 0
    for j in range(number_of_trials):
        x = []
        for i in range(number_of_students):
            s = []
            day = random.randint(1, 30)
            month = random.randint(1, 12)
            s.append(day)
            s.append(month)
            x.append(s)
            #print(f"{s}")
        # print(x)
        x2 = sorted(x)
        # print(x2)
        for i in range(len(x2) - 1):
            if x2[i] == x2[i + 1]:
                count += 1         #checking only one pair is enough for a single trial
                # print (x2[i])
                break
    probability=(count/number_of_trials)*100
    print (probability)
    return probability

birthday_paradox(23,1000)
