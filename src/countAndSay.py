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
    print('length '+str(length))
    result = ''
    i = 0
    while i < length:
        print('i = '+str(i))
        j = i
        count = 0
        while j < length and num[j] == num[i]:
            count += 1
            j += 1
        result += str(count)
        result += num[i]
        i = j
        #print('2i = '+str(i))
        if i >= length:
            break
    #print(result)
    return result
print(sayOneNumber('111221'))
print(countAndSay(2))
