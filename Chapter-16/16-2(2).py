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
        values = input("Enter your birth year, month and day sperated by space:\n").split()
        try:
            year, month, day = map(int, values)  # converts string input to integer
            if birthday_validation(year, month, day):
                return datetime.date(year, month, day)
            else:
                print("invalid  date, try again")
        except ValueError:
            print("invalid format, numbers only")
def leap_year(year):
    if (year%4==0 and year%100 !=0) or (year%400==0):
        return True
    return False
def next_leap_year(year):
    """
    Find the next leap year that supports February 29.
    """
    while not leap_year(year):
        year += 1
    return year
def age(birth_date):
    today_date=datetime.date.today()
    age=today_date.year - birth_date.year
    if (birth_date.month,birth_date.day) > (today_date.month,today_date.day):
        age-=1
    return age
def remaining_time(year,month,day):
    next_birthdate = datetime.datetime(year, month, day)
    remaining = abs(next_birthdate - datetime.datetime.now())
    return remaining

def countdown(y,birth_date):
    #birth_date=birthday_input()
    birth_month = birth_date.month
    birth_day = birth_date.day
    if datetime.date.today()>datetime.date(y,birth_month,birth_day):
        if birth_month == 2 and birth_day == 29:
            next_year = next_leap_year(y + 1)
            return remaining_time(next_year, 2, 29)
        return remaining_time(y + 1, birth_month, birth_day)
    elif datetime.date.today()<datetime.date(y,birth_month,birth_day):
        if birth_month == 2 and birth_day == 29:
            this_year = next_leap_year(y)
            return remaining_time(this_year, 2, 29)
        return remaining_time(y, birth_month, birth_day)
    else:
        return "Happy birthday!"

if __name__=="__main__":

    birth_date=birthday_input()
    print(birth_date)
    today_date = datetime.datetime.now()
    print(today_date)
    y = today_date.year
    print(f"{countdown(y,birth_date)} to celebrate!")
    print(f"{age(birth_date)} years old")
