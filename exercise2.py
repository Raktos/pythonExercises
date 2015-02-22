__author__ = 'Raktos'

def max_of_three(x,y,z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

print(max_of_three(7,2,3))
