# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        big = float("-inf")

        def dfs(root):
            nonlocal big
            if root == None:
                return float("-inf")
            
            left = dfs(root.left)
            right = dfs(root.right)
            big = max(big, root.val, root.val + left, root.val + right, root.val + left + right, left, right)

            root.val = max(root.val, root.val + left, root.val + right)
            return root.val

        dfs(root)
        return big