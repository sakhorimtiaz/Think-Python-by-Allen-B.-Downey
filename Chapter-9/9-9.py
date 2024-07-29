#process: 1 (from given solution)
def checking_reverse(i,j):
    person_1_age=str(i).zfill(2)
    person_2_age=str(j).zfill(2)
    return person_1_age==person_2_age[::-1]
#chekning the number of instances, how many times the ages are reversed for an age differnce
#the number occurrences should be 8
def number_of_occurrence(diff,flag=False):
    son_age=0
    count=0
    while True:
        mother_age = son_age + diff
        if checking_reverse(son_age,mother_age):
            count=count+1
            if flag:
                print(f"son's age: {son_age} and mother's age: {mother_age}")
        if mother_age>120:
            break
        son_age=son_age+1
    #print(count) # we need to find out 8 occurrences according to the question.
    return count
#number_of_occurrence(18,True)

def checking_difference(): # we will take decision from this output,which age difference (in this case 8) should considered,
    diff=7
    while diff<70:
        n=number_of_occurrence(diff,False)  # checking the return value
        if n>0:
            print (f"when age difference is: {diff}; it occurs {n} times")
        diff=diff+1
checking_difference()


#process: 2
#differnec of any number and it's reverse is the multiple of 9.
#example: 21-12=9, 53-35=18, 52-25=27, 02-20=18,
"""def reverse(age):
    s = str(age).zfill(2)
    reverse_age_string=s[::-1]
    reverse_age_int=int(reverse_age_string)
    return reverse_age_int

def age_checking():
    for i in range(100):
        for son_age in range(100): #consider the son's age will be less that 100
            mother_age = son_age + 9 * i
            age_difference=(mother_age-son_age)
            if mother_age == reverse(son_age):
                print(f"son:{son_age},mother:{mother_age},age differnec:{age_difference}")

    print()
age_checking()"""

#process-2:
"""def reverse(age):
    #Returns the reverse of the age as an integer.
    return int(str(age).zfill(2)[::-1])

def find_reversible_ages_with_constant_difference():
    #Finds all pairs of ages where the son's age reversed equals the mother's age and the age difference remains constant.
    age_difference = 0
    while age_difference < 100:  # Setting an arbitrary limit to find pairs within a reasonable age range
        found_any = False
        for son_age in range(100):  # Assuming the son's age won't be more than 100
            mother_age = reverse(son_age)
            if son_age < mother_age < 100 and (mother_age - son_age) == age_difference:
                print(f"Son: {son_age}, Mother: {mother_age}, Age Difference: {age_difference}")
                found_any = True
        if found_any:
            print()
        age_difference += 1

# Run the function
find_reversible_ages_with_constant_difference()"""
