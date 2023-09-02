# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        curMax = nums[0]
        index = 0
        for i in range(1, len(nums)):
            if nums[i] > curMax:
                curMax = nums[i]
                index = i
        root = TreeNode(curMax)
        root.left = self.constructMaximumBinaryTree(nums[: index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1: ])
        return root