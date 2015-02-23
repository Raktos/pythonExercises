__author__ = 'Raktos'

def translate(str):
    newStr = ''
    for c in str:
        if not is_vowel(c) and not is_punctuation(c):
            newStr += (c + 'o' + c.lower())
        else:
            newStr += c
    return newStr


def is_vowel(char):
    vowels = ['a','e','i','o','u']

    for v in vowels:
        if char == v:
            return True
    return False

def is_punctuation(char):
    punctuation = ['!', ',', '.', ';', ':', ' ', '?']

    for p in punctuation:
        if char == p:
            return True
    return False

print(translate('This is fun!'))