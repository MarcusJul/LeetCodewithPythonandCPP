# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def detectsum(node, csum, tar):
            if node.left==None and node.right==None:
                if node.val+csum==tar:
                    return True
                else:
                    return False
            elif node.left==None and node.right!=None:
                return detectsum(node.right, csum+node.val, tar)
            elif node.left!=None and node.right==None:
                return detectsum(node.left, csum+node.val, tar)
            else:
                if detectsum(node.left, csum+node.val, tar):
                    return True
                else:
                    if detectsum(node.right, csum+node.val, tar):
                        return True
                    else:
                        return False
        if root==None:
            return False
        return detectsum(root,0,sum)
                    