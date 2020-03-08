# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None or head.next.next==None:
            return head
        
        odd_start, even_start = head, head.next
        last_odd, last_even = odd_start, even_start
        cnode = head.next.next
        odd = True
        while(cnode!=None):
            if odd:
                next_node = cnode.next
                last_odd.next = cnode
                last_odd = cnode
                cnode = next_node
                odd=False
            else:
                next_node = cnode.next
                last_even.next = cnode
                last_even = cnode
                cnode = next_node
                odd=True
        last_odd.next = even_start
        last_even.next = None
        return odd_start
            