# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def detectsum(node, csum, tar, pathlst,ret_lst):
            if node.left==None and node.right==None:
                if node.val+csum==tar:
                    ret_lst.append(pathlst+[node.val]) # don't return appended statement directly
                    return ret_lst
                else:
                    return ret_lst
            elif node.left!=None and node.right==None:
                return detectsum(node.left, csum+node.val, tar, pathlst+[node.val],ret_lst)
            elif node.left==None and node.right!=None:
                return detectsum(node.right, csum+node.val, tar, pathlst+[node.val],ret_lst)
            else:
                ret_lst = detectsum(node.left, csum+node.val, tar, pathlst+[node.val],ret_lst)
                return detectsum(node.right, csum+node.val, tar, pathlst+[node.val],ret_lst)
        if root==None:
            return []
        return detectsum(root, 0, sum, [], [])
        