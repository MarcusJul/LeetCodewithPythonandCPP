# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head==None:
            return [0]
        
        # Starting from the last one
        # First calculate the max and construct the list
        # Move backward with recursion and updat
        # lnode is the node after current node, but remember you are doing backward
        def get_min_larger(num, lst):
            for i in lst:
                if num<i:
                    return i
            
        def GetFirstLarger(cnode,lnode):
            if cnode.next==None: 
                return [0], 0
            ret_lst, pmax = GetFirstLarger(cnode.next,lnode.next)
            # as long as ln.val is larger than cn.val, you should use it as greaterNode
            if lnode.val>cnode.val:
                return [lnode.val] + ret_lst, max(pmax,lnode.val)
            else: #otherwise use the old greaterNode, 
                # or if cn.val is larger than ret_lst[0], update it with 0
                if cnode.val>=pmax: #node cn.val is larger than the largest of them all
                    return [0]+ret_lst, max(pmax,lnode.val)
                else:# from left to right, find the first one that is larger than cn.val
                    return [get_min_larger(cnode.val,ret_lst)] + ret_lst, max(pmax,lnode.val)
        ret_lst, pmax = GetFirstLarger(head,head.next)    
        return ret_lst