# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        self.getPath(root, path, res)
        return res

    def getPath(self, node, path, res):
        path.append(node.val)
        if node.left is None and node.right is None:
            res.append(self.toString(path))
            return
        if node.left:
            self.getPath(node.left, path, res)
            path.pop()
        if node.right:
            self.getPath(node.right, path, res)
            path.pop()

    def toString(self, path):
        s = str(path[0])
        for i in range(1, len(path)):
            s += ("->" + str(path[i]))
        return s
