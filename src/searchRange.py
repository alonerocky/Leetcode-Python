# @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
def searchRange(A, target):
    if A == None or len(A) == 0:
        return [-1, -1]
    i = 0
    j = len(A) -1
    # find the low part
    # low point to num less than target
    # high point to num equal or bigger than target
    while i < j:
        middle = (i + j)//2
        if A[middle] >= target:
            j = middle
        else:
            i = middle + 1
    if A[j] != target:
        return [-1,-1]
    low = j
    i = low
    j = len(A) -1
    while i < j:
        middle = (i + j)//2 + 1
        if A[middle] <= target:
            i = middle
        else:
            j = middle -1
    high = i
    return [low, high]
    #print(A)

num = [5, 7, 7, 8, 8, 10]
print(searchRange(num,8))