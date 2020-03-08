# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root==None:
            return [None]*k
        if root.next==None:
            return [root]+[None]*(k-1)
        
        len_count = 0
        cnode = root
        pnode = root
        # try to get to the bottom of the list first
        while(cnode!=None):
            len_count+=1
            cnode = cnode.next
        # if k is longer than the list length, slice every one into one node
        if k>=len_count:
            ret_lst = []
            cnode = root
            for i in range(len_count):
                next_node = cnode.next
                cnode.next = None
                ret_lst.append(cnode)
                cnode = next_node
            ret_lst += [None]*(k-len_count)
            return ret_lst
        # else slice the whole into k pieces, starting from the end
        else:
            # Find the right slicing
            # Since anytwo should not have len diff larger than 1
            # First slice the whole list into k pieces
            left, no_in_each = len_count%k, len_count//k
            slice_nums = [no_in_each+1]*left+[no_in_each]*(k-left)
            
            cnode = root
            ret_lst = []
            for runlen in slice_nums:
                start_node = cnode
                for j in range(runlen):
                    if j==runlen-1:
                        next_node = cnode.next
                        cnode.next = None
                        cnode = next_node
                    else:
                        cnode = cnode.next
                ret_lst.append(start_node)
            return ret_lst
            
            
            
            