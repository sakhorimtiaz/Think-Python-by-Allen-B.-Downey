def is_power(a,b):
    #guardian
    if b==1 and a!=1:
        print ("2nd value(b) cannot be 1") # infinite loop
    elif a<b:
        print ("put the greater number 1st")
    #main code from here.
    elif a%b!=0:
        return False
    elif a==b:
        return True
    else:
        c=a//b
        #print("c",c)
        g=is_power(c,b)
        #print("c,b",c,b)
        return g
print (is_power(2,1024))
