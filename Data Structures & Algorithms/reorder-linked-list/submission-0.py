# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #slow.next = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            temp2 = prev.next
            prev.next = temp
            cur = temp
            prev = temp2

