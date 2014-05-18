'''
Created on May 18, 2014

@author: shoulongli
'''
mapping = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
def intToRoman(num):
    result = ''
    keys = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    for i in keys:
        while num >= mapping[i]:
            result += i
            num -= mapping[i]
    return result

print(intToRoman(4))
