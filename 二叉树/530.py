import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = math.inf
        return self.getMinDiff(root)

    def getMinDiff(self, root):
        if not root or (not root.left and not root.right):
            return math.inf
        m = root.val
        if root.left and root.right:
            rightMin = self.getMin(root.right)
            leftMax = self.getMax(root.left)
            self.res = min(self.res, abs(m - rightMin), abs(m - leftMax), abs(leftMax - rightMin))
        elif not root.left:
            rightMin = self.getMin(root.right)
            self.res = min(self.res, abs(m - rightMin))
        elif not root.right:
            leftMax = self.getMax(root.left)
            self.res = min(self.res, abs(m - leftMax))
        return min(self.res, self.getMinDiff(root.left), self.getMinDiff(root.right))

    def getMin(self, node):
        while node.left:
            node = node.left
        return node.val

    def getMax(self, node):
        while node.right:
            node = node.right
        return node.val

