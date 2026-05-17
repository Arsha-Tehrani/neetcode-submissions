# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = [root]
        next_que = []
        res = []
        while len(que) > 0:
            n = len(que)
            for i in range(n):
                cur = que[i]
                if cur.left:
                    next_que.append(cur.left)
                if cur.right:
                    next_que.append(cur.right)
            res.append(cur.val)

            que = next_que
            next_que = []

            
        return res
