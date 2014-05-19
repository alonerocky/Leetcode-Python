'''
Created on May 18, 2014

@author: shoulongli
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
'''
def countAndSay(n):
    if n ==1:
        return '1'
    else:
        return sayOneNumber(countAndSay(n-1))

def sayOneNumber(num):
    length = len(num)
    result = ''
    for i in range(0,length):
        j = i
        count = 0
        while j < length and num[j] == num[i]:
            count += 1
            j += 1
        result += str(count)
        result += num[i]
        i = j
        if i >= length:
            break
    #print(result)
    return result
print(sayOneNumber('111221'))
#print(countAndSay(6))
