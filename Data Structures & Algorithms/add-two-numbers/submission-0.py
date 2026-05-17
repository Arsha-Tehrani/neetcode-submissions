# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        num1 = 0
        cur2 = l2
        num2 = 0
        while cur1:
            temp = cur1.val
            if num1 == 0:
                num1 += temp
            else:
                num1 = int(str(temp) + str(num1))

            cur1 = cur1.next

        while cur2:
            temp = cur2.val
            if num2 == 0:
                num2 += temp
            else:
                num2 = int(str(temp) + str(num2))

            cur2 = cur2.next

        x = num1 + num2
        y = str(x)
        head = ListNode(int(y[len(y)-1]))
        begining = head
        for i in range(len(y)-2, -1, -1):
            begining.next = ListNode(int(y[i]))
            begining = begining.next

        print(x)
        return head
