__author__ = 'Raktos'

def char_freq(str):
    frequencies = {}
    for c in str:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    return frequencies

print(char_freq('aaaacccaccfdsafdsagrsbfdsgdsafdsagfdbvcvnmcxbzzdwuqroiepwuqioreywuio'))