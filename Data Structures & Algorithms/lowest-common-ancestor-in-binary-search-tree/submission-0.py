# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        qeue = [root]
        while len(qeue) > 0:
            right = False
            left = False
            cur = qeue.pop()
            if len(qeue) == 0 and (cur.val == p.val or cur.val == q.val):
                return cur

            #p = 4, q = 7
            if p.val > cur.val or q.val > cur.val:
                qeue.append(cur.right)
                right = True
            if p.val < cur.val or q.val < cur.val:
                qeue.append(cur.left)
                left = True

            if left and right:
                return cur
            

