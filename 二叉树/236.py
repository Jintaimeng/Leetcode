class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parents = {}
        self.parents[root] = root
        self.getParents(root)

        p_parlist = []
        p_parlist.append(p)
        t = self.parents[p]
        while t != root:
            p_parlist.append(t)
            t = self.parents[t]
        p_parlist.append(root)

        q_parlist = []
        q_parlist.append(q)
        t = self.parents[q]
        while t != root:
            q_parlist.append(t)
            t = self.parents[t]
        q_parlist.append(root)

        for pl in p_parlist:
            if pl in q_parlist:
                return pl

    def getParents(self, node):
        if node.left:
            self.parents[node.left] = node
            self.getParents(node.left)
        if node.right:
            self.parents[node.right] = node
            self.getParents(node.right)