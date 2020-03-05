# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head==None:
            return None
        
        def stackReverse(cur_node, last_node, count):
            if count!=n:
                head_node,tail_node = stackReverse(cur_node.next, cur_node, count+1)
                cur_node.next = last_node
                return head_node, tail_node
            else:
                tail_node = cur_node.next
                cur_node.next = last_node
                # when reach the end
                # tail_node is the next node after the revsersed
                # cur_node is the first node of the reversed
                return cur_node, tail_node
        
        
        
        # before you call stackReverse, cur_node is the first node of to-reversed
        # last_node is the last node before to-reversed
        if m == 1:
            cur_node = head
            head_node, tail_node = stackReverse(head, None, 1)
            cur_node.next = tail_node
            return head_node
        else:
            cur_node = head
            count = 1
            while(count!=m):
                last_node = cur_node
                cur_node = cur_node.next
                count+=1
            head_node, tail_node = stackReverse(cur_node, last_node, count)
            last_node.next = head_node
            # cur_node now become the last node of reversed
            cur_node.next = tail_node
            return head