'''
Created on May 18, 2014

@author: shoulongli
'''
#I    V    X     L    C        D    M
#1    5    10    50    100    500    1000
mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def romanToInt(s):
    length = len(s)
    result = 0
    for i in range(0,length):
        cur = char2num(s[i])
        c2 = 0
        if i < length -1:
            c2 = char2num(s[i+1])
        if cur < c2:
            result -= cur
        else:
            result += cur
    return result

def char2num(c):
    c = c.upper()
    if c in mapping:
        return mapping[c]
    else:
        return 0
print(char2num('D'))
print(romanToInt('IV'))
