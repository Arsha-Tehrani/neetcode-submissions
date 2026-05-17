# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count += 1
        top = root.val
        self.digMax(root.left, top)
        self.digMax(root.right, top)
        return self.count
            

    def digMax(self, node, top):
        if not node: return None
        if node.val >= top:
            self.count += 1
            top = node.val

        return self.digMax(node.left, top) or self.digMax(node.right, top)
