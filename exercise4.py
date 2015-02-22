__author__ = 'Raktos'

def is_vowel(char):
    vowels = ['a','e','i','o','u']

    for v in vowels:
        if char == v:
            return True
    return False

print(is_vowel('a'))
print(is_vowel('g'))