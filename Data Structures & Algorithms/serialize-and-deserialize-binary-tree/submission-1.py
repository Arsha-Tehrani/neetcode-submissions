import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                # Append children even if they are None; the next iteration handles the "N"
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
                
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        
        # Pointer to track our position in the vals array
        i = 1 
        
        while queue:
            node = queue.popleft()
            
            # Reconstruct left child
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            
            # Reconstruct right child
            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
            
        return root