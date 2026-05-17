# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None: return 0
        num = 1
        left_branch = self.dig(root.left, num)
        right_branch = self.dig(root.right, num)

        return max(left_branch, right_branch)

    def dig(self, root: Optional[TreeNode], num:int) -> int:

        if root == None:
            return num
        num += 1

        if root.left and root.right:
            return max(self.dig(root.right, num), self.dig(root.left, num))
        elif root.left:
            return self.dig(root.left, num)
        elif root.right:
            return self.dig(root.right, num)
        else:
            return num