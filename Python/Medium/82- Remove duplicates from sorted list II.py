# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        val_dict = {}
        cur_node = head
        while(cur_node!=None):
            if cur_node.val in val_dict:
                val_dict[cur_node.val] += 1
            else:
                val_dict[cur_node.val] = 1
            cur_node = cur_node.next
        
        start = None
        cur_node = None
        for k,v in val_dict.items():
            if v == 1:
                if start == None:
                    start = ListNode(k)
                    cur_node = start
                else:
                    next_node = ListNode(k)
                    cur_node.next = next_node
                    cur_node = next_node
        return start
        
    