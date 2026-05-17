# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        unsort1 = []
        cur2 = list2
        unsort2 = [] 


        while cur1:
            unsort1.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            unsort2.append(cur2.val)
            cur2 = cur2.next

        res = []
        a = len(unsort1)
        b = len(unsort2)
        r,l = 0,0

        while l < a and r < b:
            if unsort1[l] < unsort2[r]:
                res.append(unsort1[l])
                l += 1
            else:
                res.append(unsort2[r])
                r += 1

        res.extend(unsort1[l:])
        res.extend(unsort2[r:])

        if res: 
            dummy = ListNode(res.pop(0))
            cur = dummy
            for val in res:
                cur.next = ListNode(val)
                cur = cur.next
            
            return dummy
        
        return list1
