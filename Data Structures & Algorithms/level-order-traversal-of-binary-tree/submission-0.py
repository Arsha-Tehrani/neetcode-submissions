# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = [root]
        while len(que) > 0:
            next_que = []
            n = len(que)
            temp = []
            for i in range(n):
                cur = que[i]
                temp.append(cur.val)
                if cur.left:
                    next_que.append(cur.left)
                if cur.right:
                    next_que.append(cur.right)

            res.append(temp)
            temp = []
            que = next_que
            next_que = []

        return res
        


