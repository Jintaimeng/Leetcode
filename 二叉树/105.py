class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.building(preorder, inorder)

    def building(self, preorder, inorder):
        inorder_map = dict()
        preorder_map = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        for i in range(len(preorder)):
            preorder_map[preorder[i]] = i
        if preorder is None or inorder is None:
            return
        in_node = preorder[0]
        in_index = inorder_map[in_node]
        if in_index <= 0:
            left_nodes = None
        else:
            left_nodes = self.building(preorder[1: in_index+1], inorder[0: in_index])
        if len(inorder) - 1 - in_index <= 0:
            right_nodes = None
        else:
            right_nodes = self.building(preorder[in_index + 1: ], inorder[in_index+1: ])
        node = TreeNode(in_node, left_nodes, right_nodes)
        return node

