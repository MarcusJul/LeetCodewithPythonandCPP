# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #solution 1
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Instead of combine and sort, sort for eveyone before and compare
        def insertsortLinkedList(head):
            if head==None or head.next==None:
                return head
            sl = head # take the first element as the sorted list to start with
            cnode = head.next
            head.next = None # detach the sorted list from the rest
            while(cnode!=None):
                tnsl = sl #traverse node in the sorted list
                nnode = cnode.next #next node
                pre_tnsl = None # the node before tnsl
                flag = False
                while(tnsl!=None):
                    if cnode.val<=tnsl.val:
                        if pre_tnsl==None: #cnode is the smallest in the list
                            cnode.next = sl
                            sl = cnode # use cnode as the new start
                        else:
                            pre_tnsl.next = cnode
                            cnode.next = tnsl
                        break
                    else:
                        pre_tnsl = tnsl
                        tnsl = tnsl.next
                # special case where cnode is larger than any in the list
                # it becomes the last one in the list
                if tnsl==None:
                    if pre_tnsl.val<=cnode.val:
                        pre_tnsl.next = cnode
                        cnode.next = None
                cnode = nnode
            return sl
        
        def findend(head):
            if head==None:
                return head
            cnode = head
            while(cnode.next!=None):
                cnode = cnode.next
            return cnode
        # find the first list that is not Null
        total_head = None
        flag, endnode = False, None
        for lst in lists:
            if flag==False:
                if lst==None:
                    continue
                else:
                    total_head = lst
                    flag = True
            if lst==None:
                continue
            if endnode==None:
                pass
            else:
                endnode.next = lst
            endnode = findend(lst)
            
        return insertsortLinkedList(total_head)
    #solution 2
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cd = {} #counting dict
        # traverse the linked list and record what's in
        def traverseArecord(cd, lst):
            if lst==None:
                return cd
            cnode = lst
            while(cnode!=None):
                if cnode.val in cd:
                    cd[cnode.val] +=1
                else: 
                    cd[cnode.val] = 1
                cnode = cnode.next
            return cd
        for lst in lists:
            cd = traverseArecord(cd, lst)
        
        # rank the dict by keys and create 
        if cd=={}:
            return None
        ret_start, endoflast = None, None
        keys = sorted(cd.keys())
        def createLinkedList(val, num):
            head = ListNode(val)
            if num==1:
                return head, head
            cnode = head
            for i in range(1,num):
                node = ListNode(val)
                cnode.next = node
                cnode = node
            
            return head, cnode 
        
        for key in keys:
            if ret_start==None:
                ret_start, endoflast= createLinkedList(key,cd[key])
            else:
                lst_start, endnode = createLinkedList(key,cd[key])
                endoflast.next = lst_start
                endoflast = endnode
        return ret_start
        