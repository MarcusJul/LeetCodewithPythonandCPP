# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        def retDepth(root, cur_depth):
            
            left_d = retDepth(root.left, cur_depth+1) if root.left!=None else cur_depth
            right_d = retDepth(root.right, cur_depth+1) if root.right!=None else cur_depth
            return max(left_d, right_d)
        
        return retDepth(root, 1)