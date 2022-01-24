class Solution:
   
    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)