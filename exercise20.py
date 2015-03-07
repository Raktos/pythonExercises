__author__ = 'Raktos'

#expects an array of words for str
def translate(words, lexicon):
    for i in range(0, len(words), 1):
        if words[i] in lexicon:
            words[i] = lexicon[words[i]]
    return words

lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}

print(translate(['merry', 'bob'], lexicon))