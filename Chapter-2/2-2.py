#exercise 2.2 Q-2
n=24.95
m= round (n- (n*(40/100)))
p=60
print ("price of 60 boks is", m*p+3+(p-1)*(75/100))
print (m*p)

#exercise 2.2 Q-3
start = 6*60+52
s=2*(8*60+15)+3*(7*60+12)
m=s//60 #sec to min, only minutes, places before the decimal point, 
n=s%60  # only sec part, places after the decimal

if m<8 :
    print ("6 :",52+m,":",n,"AM")
elif m==8:
    print ("7 :",m-8,":",n,"AM")
elif m%68==0:
    print (7+(m//68)," : 0 :",n,"AM")
elif m>8 and m%68!=1:
    print (7+(m//68),":",m%68-8,":",n,"AM")

print (s,m,n)
