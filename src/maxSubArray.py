'''
Created on Jun 25, 2014

@author: shoulongli
'''
def maxSubArray( A):
        curSum = A[0]
        maxSum = A[0]
        for i in range(1,len(A)):
            if curSum < 0:
                curSum = 0
            curSum += A[i]
            maxSum = max(maxSum,curSum)
        return maxSum