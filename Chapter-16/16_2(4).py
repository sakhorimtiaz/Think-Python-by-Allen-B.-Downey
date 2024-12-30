import datetime
def birthday_validation(year, month, day):
    today=datetime.date.today()
    try:
        birth_date=datetime.date(year,month,day)
        if birth_date<=today:
            return True
        return False
    except ValueError:
        return False
def birthday_input():
    while True:
        values = input("Enter your birth year, month and day separated by space:\n").split()
        try:
            year, month, day = map(int, values)  # converts string input to integer
            if birthday_validation(year, month, day):
                return datetime.date(year, month, day)
            else:
                print("invalid  date, try again")
        except ValueError:
            print("invalid format, numbers only")
def nth_day(user_1,user_2,n):
    if user_1==user_2:
        print("same date")
        return user_1
    s = sorted([user_1, user_2])
    earlier, later=s[0],s[1]
    difference=later-earlier
    print(difference)
    print(difference.days)
    increment=difference.days/(n-1)
    nth_day_date=later+datetime.timedelta(days=increment)
    return nth_day_date

if __name__=="__main__":
    user_1=birthday_input()
    user_2=birthday_input()
    n=int(input("enter the nth value:"))
    s = sorted([user_1, user_2])
    d=nth_day(user_1, user_2,n)
    print(d)
    print(d-s[0])
    print(d-s[1])
