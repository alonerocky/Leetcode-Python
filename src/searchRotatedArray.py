def search(A, target):
    if A == None or len(A) == 0:
        return -1
    i = 0
    j = len(A) -1
    while i <= j:
        middle = (i + j)//2
        if target == A[middle]:
            return middle
        elif A[i] <= A[middle]: # left side is sorted
            if A[i] <= target and target < A[middle]: # located in left side
                j = middle - 1
            else:
                i = middle + 1
        else:
            if A[middle] < target and target <= A[j]: # located in right side
                i = middle + 1
            else:
                j = middle -1
    return -1

num = [4 ,5 ,6, 7 ,0 ,1, 2]
print(search(num, 7))
print(search(num,3))