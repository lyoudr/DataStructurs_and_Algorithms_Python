# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right


class Solution:
    def bfs_traverse(self, root, res):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                if node.left.val > node.val:
                    queue.append(node.left)
            if node.right:
                if node.right.val < node.val:
                    queue.append(node.right)
    
    def validate(self, root, min, max):
        if root == None:
            return True
        if min != None and root.val <= min or max != None and root.val >= max:
            return False
        return self.validate(root.right, root.val, max) and self.validate(root.left, min, root.val)

    def inorder_traverse(self, node, res):
        if node.left:
            self.inorder_traverse(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorder_traverse(node.right, res)

    def isValidBST(self, root) -> bool:
        res = []
        self.bfs_traverse(root, res)
        print('res is =>', res)



class Solution:
    def is_symmetric(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        
        return left.val == right.val and self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return True
        return self.is_symmetric(root.left, root.right)


