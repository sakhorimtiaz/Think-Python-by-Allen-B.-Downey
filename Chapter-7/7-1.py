import math
def mysqrt(a):
    x=a/2 #guess a value
    while True:
        y = 0.5 * (x + a / x)  #Newton's law to calculate square root
        if y == x:
            break
        x = y
    return y
def diff(a):
    c2 = mysqrt(a)
    c3 = math.sqrt(a)
    return abs(c2-c3)
def test_square_root(a):
    print("a  ", "mysqrt(a)            ", "math.sqrt(a)         ", "diff")
    print("-   --------              -----------           ----")

    for i in range(9):
        print("%.1f %.19f %.19f %f" % (a,mysqrt(a),math.sqrt(a),diff(a)))  #%.19f means we will consider 19 decimal places
        a=a+1
test_square_root(2)
