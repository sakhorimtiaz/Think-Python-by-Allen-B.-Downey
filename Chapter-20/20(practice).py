def infinite_loop_debugging(x,y):
    while x > 0 and y < 0:
        print("x:",x)
        print("y:",y)
        print("conditions;",(x>0 and y<0))
        x -= 1  # Decrease x
        y += 1
#infinite_loop_debugging(3,-6)

import pdb

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        pdb.set_trace()  # Inspect each iteration
        result *= i
    return result

print(factorial(5))


