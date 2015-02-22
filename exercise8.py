__author__ = 'Raktos'

def is_palindrome(str):
    return str == reverse(str)

def reverse(str):
    rev = ''
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]
    return rev

print(is_palindrome('abba'))
print(is_palindrome('abssrsrrssrsssssrba'))