'''
Created on May 12, 2014

@author: shoulongli
'''
def removeDuplicates(A):
    if A == None or len(A) == 0:
        return 0
    length = len(A)
    i = 0
    while i < length:
        j = i
        while j < length and A[j] == A[i]:
            j += 1
        duplicates = j - i
        if j == length:
            return i
        #i, j-1
        #i+1, j
        if duplicates > 1:
            arrayCopy(A,j,A,i + 1, duplicates-1 )
            length -= duplicates - 1
        i += 1
    return length

def arrayCopy(source, sourcepos, dest, destpos, numelem):
    dest[destpos:destpos + numelem] = source[sourcepos:sourcepos + numelem]

num = [1,1,2,2,3]
print(num)
print(removeDuplicates(num))
print(num)