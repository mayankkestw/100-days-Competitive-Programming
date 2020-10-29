# Recursive

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Iterative

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        d = 0
        
        if root==None:
            return d
        
        q = [root]
        
        while q:
            d+=1
            for _ in range(len(q)):
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return d