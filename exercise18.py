__author__ = 'Raktos'

def is_pangram(str):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #for maximum efficiency sort by letter frequency in target language
    for c in str.lower():
        for l in letters:
            if l == c:
                letters.remove(l)
    return letters == []

print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('ahgfdreswgre'))