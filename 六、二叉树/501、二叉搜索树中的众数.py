from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.pre = None
        self.count = 0
        self.maxCount = 0
        self.findM(root)
        return self.res

    def findM(self, node):
        if node is None:
            return
        self.findM(node.left)
        if self.pre is None:
            self.count = 1
        elif self.pre and node.val == self.pre.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = node
        if self.count == self.maxCount:
            self.res.append(node.val)
        elif self.count > self.maxCount:
            self.maxCount = self.count
            self.res.clear()
            self.res.append(node.val)
        self.findM(node.right)