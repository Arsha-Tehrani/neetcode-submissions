# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        
        top = root
        stack = []
        stack.append(top)

        while len(stack) > 0:
            cur = stack.pop()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
        
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return root