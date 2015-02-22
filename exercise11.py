__author__ = 'Raktos'

def generate_n_chars(n,c):
    str = ''
    for i in range(0,n,1):
        str += c
    return str

print(generate_n_chars(5,'x'))