# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #Maintain a min and max variable. Run it in one command
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dig_left(root, -9999999, 9999999)
        
    def dig_left(self, root, low, high):
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        val = root.val
        
        return self.dig_left(root.left, low, root.val) and self.dig_left(root.right, root.val, high)
    
    