class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        n = len(inorder)
        for i in range(n):
            dict[inorder[i]] = i
        return self.getTree(preorder, 0, n - 1, dict, 0, n - 1)

    def getTree(self, preorder, preLeft, preRight, dict, inLeft, inRight):
        if preLeft > preRight or inLeft > inRight:
            return None
        rootVal = preorder[preLeft]
        root = TreeNode(rootVal)
        pIndex = dict[rootVal]
        root.left = self.getTree(preorder, preLeft + 1, pIndex - inLeft + preLeft, dict, inLeft, pIndex - 1)
        root.right = self.getTree(preorder, pIndex - inLeft + preLeft + 1, preRight, dict, pIndex + 1, inRight)
        return root