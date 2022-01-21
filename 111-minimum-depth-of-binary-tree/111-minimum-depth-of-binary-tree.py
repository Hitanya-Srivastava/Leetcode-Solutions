class Solution:
    
    def is_leaf(self, node):
        return not node.left and not node.right
    
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        if self.is_leaf(root): return 1
        
        queue = deque([(root,1)])
        while queue:
            curr, count = queue.popleft()
            if self.is_leaf(curr):
                    return count
            
            if curr.left:
                queue.append((curr.left, count+1))
            
            if curr.right:
                queue.append((curr.right, count+1))