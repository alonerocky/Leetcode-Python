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

    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree_inorder_poster(self, inorder, postorder):
        return self.buildTree_inorder_poster_helper(inorder,0,len(inorder) -1, \
                                                    postorder,0,len(postorder)-1)

    def buildTree_inorder_poster_helper(self,inorder, istart,iend,postorder,pstart,pend):
        if (inorder == None or \
            len(inorder) == 0 or \
            postorder == None or \
            len(postorder) == 0 or \
            istart > iend or \
            pstart > pend or \
            iend - istart != pend - pstart \
            ):
            return None
        root  = postorder[pend]
        result = TreeNode(root)
        # postorder: [pstart,  pend -1]
        # find index in inorder array
        index = self.getIndex(inorder,istart,iend,root)
        if index == -1:
            return result
        # inorder[index] == root
        # istart, index -1 : left
        # index + 1 , iend : right

        # pstart,  x : left
        # x +1,   pend - 1: right

        # x: x  - pstart = index -1 - istart
        #    x = index -1 + pstart - istart
        # pend -1 - x -1 = iend - index-1
        # x = pend - iend + index -1
        pindex = index -1 + pstart - istart
        result.left = self.buildTree_inorder_poster_helper(inorder, istart, index -1,\
                                                           postorder, pstart, pindex )
        result.right = self.buildTree_inorder_poster_helper(inorder, index + 1, iend, \
                                                            postorder, pindex + 1, pend -1)


        return result

    def getIndex(self, array, start, end,target):
        if array == None or start > end :
            return -1
        for i in range(start,end + 1):
            if array[i] == target:
                return i
        return -1

    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree_preorder_inorder(self, preorder, inorder):
        return self.buildTree_preorder_inorder_helper(preorder,0,len(preorder) -1, inorder,0,len(inorder) -1)
    def buildTree_preorder_inorder_helper(self,preorder,pstart,pend,inorder,istart,iend):
        if preorder == None or \
        len(preorder) == 0 or \
        inorder == None or \
        len(inorder) == 0 or \
        pstart > pend or \
        istart > iend or \
        pend - pstart != iend - istart:
            return None
        root = preorder[pstart]
        result = TreeNode(root)
        # [pstart + 1, pindex] : left
        # [pindex + 1, pend]   : right
        index = self.getIndex(inorder, istart, iend, root)
        if index == -1:
            return result
        # istart, index - 1: left
        # index + 1, iend:   right
        # pindex - pstart -1 = index - 1 - istart
        pindex = pstart - istart + index
        # pend - pindex - 1 = iend - index -1
        result.left = self.buildTree_preorder_inorder_helper(preorder, pstart + 1, pindex, inorder, istart, index -1)
        result.right = self.buildTree_preorder_inorder_helper(preorder, pindex + 1, pend, inorder, index + 1, iend)
        return result

inorder = [1,2]
postorder = [2,1]
root = TreeNode(0)
root.buildTree_inorder_poster(inorder,postorder)

