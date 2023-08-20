# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = []
        curNode = root
        while stack or curNode:
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                node = stack.pop()
                res.append(node.val)
                curNode = curNode.right
        return res


