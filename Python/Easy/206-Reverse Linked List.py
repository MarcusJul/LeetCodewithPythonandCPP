# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        store = []
        cur_node = head
        while(cur_node!=None):
            store.append(cur_node)
            cur_node = cur_node.next
        head_node, cur_node = store[-1],store[-1]
        store = list(reversed(store))
        
        while(True):
            store = store[:-1]
            if store==[]:
                break
            else:
                cur_node.next = store[-1]
                cur_node = store[-1]
                
        cur_node.next = None
        return head_node