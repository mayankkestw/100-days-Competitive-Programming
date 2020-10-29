# Iterative

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return res[::-1]



# Recursive

class Solution:
    def helper(self, node, res):
        if node==None:
            return
        
        self.helper(node.left, res)
        self.helper(node.right, res)
        res.append(node.val)
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        self.helper(root, res)
        
        return res