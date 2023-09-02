# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        leftInorder = inorder[: index]
        leftPostorder = postorder[: len(leftInorder)]
        rightInorder = inorder[index + 1: ]
        rightPostorder = postorder[len(rightInorder) + 1: ]
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        return root