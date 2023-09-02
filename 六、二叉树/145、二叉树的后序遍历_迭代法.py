# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = []
        stack.append(root)
        while stack:
            curNode = stack.pop()
            res.append(curNode.val)
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
        res.reverse()
        return res

