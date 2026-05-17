# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        dummy = ListNode(0)
        tail = dummy
        if n == 0:
            return None
        cur1 = lists[0]
        for i in range(1,n):
            cur2 = lists[i]
            while cur1 and cur2:
                if cur1.val <= cur2.val:
                    tail.next = cur1
                    cur1 = cur1.next
                else:
                    tail.next = cur2
                    cur2 = cur2.next
                
                tail = tail.next

            tail.next = cur1 or cur2
            cur1 = dummy.next

            dummy = ListNode(0)
            tail = dummy

        return cur1
                
                    