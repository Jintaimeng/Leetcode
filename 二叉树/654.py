class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        maxValue = max(nums)
        index = nums.index(maxValue)
        root = TreeNode(maxValue)
        root.left = self.constructMaximumBinaryTree(nums[: index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1: ])
        return root
