class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res_str = []
        if not root:
            return []
        if not root.left and not root.right:
            res_str.append(str(root.val))
            return res_str
        for i in self.binaryTreePaths(root.left):
            res_str.append(str(root.val) + "->" + i)
        for j in self.binaryTreePaths(root.right):
            res_str.append(str(root.val) + "->" + j)
        return res_str