'''
Created on Jun 16, 2014

@author: shoulongli
'''
def plusOne(digits):
    if digits == None or len(digits) == 0:
        return [1]
    length = len(digits)
    index = length -1
    carray = 0
    result = []
    while index >= 0:
        sum = 0
        if index == length -1:
            sum = digits[index] + 1
        else:
            sum = digits[index] + carray

        carray = sum // 10
        result.insert(0,sum % 10)
        index -= 1

    if carray == 1:
        result.insert(0,1)

    return result

digits = [0]
print(plusOne(digits))

