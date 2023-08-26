# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dict = {}
        self.getParent(root, p, q)
        pParent = self.dict[p]
        qParent = self.dict[q]
        while pParent != qParent:
            pParent = self.dict[pParent]
            qParent = self.dict[qParent]
        return pParent

    def getParent(self, node, p, q):
        if node is None:
            return
        self.dict[node] = node
        if node.left and (p.val < node.val or q.val < node.val):
            self.dict[node.left] = node
            self.getParent(node.left, p, q)
        if node.right and (p.val > node.val or q.val > node.val):
            self.dict[node.right] = node
            self.getParent(node.right, p, q)