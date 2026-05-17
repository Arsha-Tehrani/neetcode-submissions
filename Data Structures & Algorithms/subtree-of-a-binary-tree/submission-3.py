# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val == subRoot.val:
                sub_stack = [subRoot]
                copy = [cur]
                while len(sub_stack) > 0 and len(copy) > 0:
                    main = copy.pop()
                    sub = sub_stack.pop()
                    checker = True
                    if sub and not main:
                        checker = False
                        break
                    elif main and not sub:
                        checker = False
                        break
                    if main and sub and main.val != sub.val:
                        checker = False
                        break
                    if main and sub:  
                        copy.append(main.right)
                        copy.append(main.left)
                        sub_stack.append(sub.right)
                        sub_stack.append(sub.left)

                if checker and len(sub_stack) == 0 and len(copy) == 0:
                    return True

            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

        return False
        