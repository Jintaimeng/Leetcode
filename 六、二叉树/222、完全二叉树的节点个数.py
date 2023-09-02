# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        h = self.isFull(root)
        if h != -1:
            return pow(2, h) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def isFull(self, root):
        count_left = 0
        count_right = 0
        p = root
        q = root
        while p:
            count_left += 1
            p = p.left
        while q:
            count_right += 1
            q = q.right
        if count_left == count_right:
            return count_left
        return -1