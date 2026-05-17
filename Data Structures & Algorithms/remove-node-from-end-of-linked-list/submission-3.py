# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        if n == 1 and cur.next:
            while cur.next and cur.next.next:
                cur = cur.next
            cur.next = None
            return head
        elif n == 1 and not cur.next:
            cur = None
            return cur
        
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp


        count = 1
        start = prev
        cur = prev
        prev = None
        while cur:
            if n == 1:
                cur = None
                break
            if count == n and not cur.next:
                prev.next = None
                break
            elif count == n:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            count += 1


        cur = start
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
