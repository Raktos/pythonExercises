__author__ = 'Raktos'

def map_words(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

print(map_words(['abc','dddd','lotsofletters']))