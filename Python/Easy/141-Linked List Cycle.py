# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        if head.next==head:
            return True
        cnode = head
        fast = cnode
        slow = cnode
        try:
            while(True):
                fast = fast.next.next
                slow = slow.next
                if fast==None or slow==None:
                    return False
                if fast==slow:
                    return True
            
        except:
            return False
                
                