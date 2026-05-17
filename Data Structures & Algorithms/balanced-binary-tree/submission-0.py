# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que = [root]
        while len(que) > 0:
            cur = que.pop()
            dig1 = self.dig(cur.left, 0)
            dig2 = self.dig(cur.right, 0)
            if abs(dig1-dig2) > 1:
                return False

            if cur.right:
                que.append(cur.right)
            if cur.left:
                que.append(cur.left)
        
        return True

    def dig(self, node: Optional[TreeNode], num: int) -> int:
        if not node:
            return num
        num += 1

        if node.left and node.right:
            return max(self.dig(node.left, num), self.dig(node.right, num))
        elif node.left:
            return self.dig(node.left, num)
        else:
            return self.dig(node.right, num)