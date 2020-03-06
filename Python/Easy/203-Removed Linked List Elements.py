# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return None
        if head.next==None:
            if head.val==val:
                return None
            else:
                return head
        # Make sure the first one is not val
        cnode=head
        while(cnode.val==val):
            head = cnode.next
            cnode = head
            if cnode==None:
                return None #All the nodes are removed
            
        cnode = head.next
        pnode = head
        while(cnode!=None):
            if cnode.val==val:
                pnode.next = cnode.next
                cnode = cnode.next
            else:
                pnode = cnode
                cnode = cnode.next
        
        return head