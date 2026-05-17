# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        cur = head

        while True:
            # --- your "test / fast" idea kept ---
            test = prev_group
            fast = 0
            while test and fast < k:
                test = test.next
                fast += 1

            if not test:  # fewer than k nodes remain
                break

            # Now we have a full group
            group_end = test
            group_next = group_end.next

            # --- your reversal logic, fixed ---
            prev = group_next
            cur = prev_group.next
            slow = 0

            while slow < k:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                slow += 1

            # --- reconnect group ---
            temp = prev_group.next
            prev_group.next = group_end
            prev_group = temp

        return dummy.next