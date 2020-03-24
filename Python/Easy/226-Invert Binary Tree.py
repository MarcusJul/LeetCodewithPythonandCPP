# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        def invertN(root):
            if root.left!=None:
                root.left = invertN(root.left)
            if root.right!=None:
                root.right = invertN(root.right)
            root.left, root.right = root.right, root.left
            return root
        
        return invertN(root)
        