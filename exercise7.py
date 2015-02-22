__author__ = 'Raktos'

def reverse(str):
    rev = ''
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]
    return rev

print(reverse('abcd'))