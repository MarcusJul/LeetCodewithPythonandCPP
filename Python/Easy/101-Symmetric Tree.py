# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #traverse the tree by in both directions, confirm the list you get are the same
        if root==None:
            return True
        if root.right==None and root.left==None:
            return True
            
        def leftTraverse(root, lst):
            lst.append(root.val)
            if root.left!=None:
                lst = leftTraverse(root.left, lst)
            else:
                lst.append(None)
            if root.right!=None:
                lst = rightTraverse(root.right, lst)
            else:
                lst.append(None)
            return lst
        
        def rightTraverse(root, lst):
            lst.append(root.val)
            if root.right!=None:
                lst = rightTraverse(root.right, lst)
            else:
                lst.append(None)
            if root.left!=None:
                lst = leftTraverse(root.left, lst)
            else:
                lst.append(None)
            return lst
        
        if leftTraverse(root,[])==rightTraverse(root,[]):
            return True
        else:
            return False