__author__ = 'Raktos'

def sing(n):
    for i in range(n, 0, -1):
        j = str(i)
        print(j + ' bottles of beer on the wall, ' + j + ' bottles of beer.')
        print('take one down, pass it around, ' + str(i - 1) + ' bottles of beer on the wall.')

sing(99)