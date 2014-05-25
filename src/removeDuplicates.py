'''
Created on May 12, 2014

@author: shoulongli
'''
def removeDuplicates(self, A):
    if A == None or len(A) == 0:
        return 0
    length = len(A)
    i = 0
    while i < length:
