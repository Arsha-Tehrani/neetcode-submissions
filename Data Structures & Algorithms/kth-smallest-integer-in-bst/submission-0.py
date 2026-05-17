# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        qeue = [root]
        nums = []
        while len(qeue) > 0:
            cur = qeue.pop()
            nums.append(cur.val)
            if cur.right:
                qeue.append(cur.right)

            if cur.left:
                qeue.append(cur.left)

        nums.sort()
        return nums[k-1]