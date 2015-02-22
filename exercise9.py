__author__ = 'Raktos'

def is_member(x, list):
    for i in list:
        if x == i:
            return True
    return False

print(is_member('a', 'spahumet'))