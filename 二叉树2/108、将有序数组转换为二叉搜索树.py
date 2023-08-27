from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        index = (len(nums) - 1) // 2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[: index])
        root.right = self.sortedArrayToBST(nums[index + 1: ])
        return root