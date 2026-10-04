# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        if cur is None:
            return TreeNode(val)
        while cur is not None:
            if val > cur.val:
                if cur.right is None:
                    break
                cur = cur.right
            elif val < cur.val:
                if cur.left is None:
                    break
                cur = cur.left

        if val > cur.val:
            cur.right = TreeNode(val)
        elif val < cur.val:
            cur.left = TreeNode(val)

        return root