__author__ = 'Raktos'

def length(list):
    count = 0
    for i in list:
        count += 1
    return count

print(length('Spahumet'))
print(length([1,2,3,4,5,1,2,3,4,5]))