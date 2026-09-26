class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to easily handle cases where left == 1
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Move prev to the node just BEFORE the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. Reverse the sublist from left to right
        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next