#递归方法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        if root is None:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.preorder(root)
        return self.res