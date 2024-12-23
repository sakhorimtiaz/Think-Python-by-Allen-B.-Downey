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
def double_day(user_1,user_2):
    if user_1==user_2:
        print("same date")       
    s = sorted([user_1, user_2])
    earlier, later=s[0],s[1]
    difference=later-earlier
    double_day_date=later+difference
    return double_day_date

if __name__=="__main__":
    user_1=birthday_input()
    user_2=birthday_input()
    s = sorted([user_1, user_2])
    d=double_day(user_1, user_2)
    print(d)
    print(d-s[0])
    print(d-s[1])
