__author__ = 'Raktos'

def max_in_list(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

print(max_in_list([1,2,3,4,5]))