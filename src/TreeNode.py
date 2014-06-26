'''
Created on Jun 16, 2014

@author: shoulongli
'''

class TreeNode(object):
    '''
    classdocs
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isBalanced(self, root):
        if root == None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1

    def getHeight(self, root):
        if root == None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left,right) + 1

    def isSameTree(self, p, q):
        if p == q:
            return True
        if p == None and q == None:
            return True
        elif p != None and q != None:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
    def flatten(self, root):
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left == None:
            return
        else:
            p = root.left
            while p.right != None:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None
            return


    def sortedArrayToBST(self, num):
        if num == None or len(num) == 0:
            return None
        return self.sortedArrayToBST_helper(num,0,len(num)-1)

    def sortedArrayToBST_helper(self,num,start,end):
        if num == None or len(num) == 0 or start > end:
            return None
        middle = (start + end) //2
        result = TreeNode(num[middle])
        result.left = self.sortedArrayToBST_helper(num,start,middle-1)
        result.right = self.sortedArrayToBST_helper(num,middle + 1, end)
        return result



