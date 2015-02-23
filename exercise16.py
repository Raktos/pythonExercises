__author__ = 'Raktos'

def filter_long_words(words, n):
    newWords = []
    for word in words:
        if len(word) > n:
            newWords.append(word)
    return newWords

print(filter_long_words(['aa','aaaaaa','aaa'], 4))