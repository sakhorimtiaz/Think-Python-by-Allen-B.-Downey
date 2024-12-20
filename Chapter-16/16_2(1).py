import datetime
def today():
    current_date = datetime.date.today()
    #print(current_date)
    day_of_the_week = current_date.weekday()
    #print(day_of_the_week)
    d={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    return d[day_of_the_week]
#print(today())
