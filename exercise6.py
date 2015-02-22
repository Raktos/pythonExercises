__author__ = 'Raktos'

def sum(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

def multiply(nums):
    product = 1
    for n in nums:
        product *= n
    return product

print(sum([1,2,3,4,5,6,7]))
print(multiply([1,2,3]))