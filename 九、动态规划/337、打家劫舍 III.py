from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.getRob(root)
        return max(res[0], res[1])

    def getRob(self, curNode):
        if curNode is None:
            return [0, 0]
        left = self.getRob(curNode.left)
        right = self.getRob(curNode.right)
        val1 = max(left[0], left[1]) + max(right[0], right[1])
        val2 = curNode.val + left[0] + right[0]
        return [val1, val2]


def main():
    root = [3,2,3,None,3,None,1]
    res = Solution().rob(root)
    print(res)


if __name__ == "__main__":
    main()