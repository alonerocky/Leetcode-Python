# @param matrix, a list of lists of integers
# @param target, an integer
# @return a boolean
def searchMatrix(matrix, target):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    rows = len(matrix)
    columns = len(matrix[0])
    i = 0
    j = columns -1
    while i < rows and j >= 0:
        element = matrix[i][j]
        if element == target:
            return True
        elif element < target:
            i += 1
        else:
            j -= 1
    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(searchMatrix(matrix,3))
print(searchMatrix(matrix,4))
print(searchMatrix(matrix,6))
print(searchMatrix([[1]],0))
