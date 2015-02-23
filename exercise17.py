__author__ = 'Raktos'

def is_palindrome(str):
    str = remove_punct(str.lower())
    return str == reverse(str)

def is_punctuation(char):
    punctuation = ['!', ',', '.', ';', ':', ' ', '?']

    for p in punctuation:
        if char == p:
            return True
    return False

def reverse(str):
    rev = ''
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]
    return rev

def remove_punct(str):
    newStr = ''
    for c in str:
        if not is_punctuation(c):
            newStr += c
    return newStr

print(is_palindrome('Was it a rat I saw?'))