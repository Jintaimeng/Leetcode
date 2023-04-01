class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            miniNode = self.findMinNode(root.right)
            root.val = miniNode.val
            root.right = self.deleteNode(root.right, miniNode.val)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root
    def findMinNode(self, node):
        while node.left:
            node = node.left
        return node