__author__ = 'Raktos'

def overlapping(x,y):
    for i in x:
        for j in y:
            if j == i:
                return True
    return False

print(overlapping([1,2,3,4,5],[6,7,8,9,1]))