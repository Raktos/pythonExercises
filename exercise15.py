__author__ = 'Raktos'

def find_longest_word(words):
    maxi = len(words[0])
    for word in words:
        length = len(word)
        if length > maxi:
            maxi = length
    return maxi

print(find_longest_word(['aa','aaaaaaa','aaa']))