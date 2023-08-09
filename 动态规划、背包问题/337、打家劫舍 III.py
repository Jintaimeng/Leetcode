from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:



def main():
    root = [3,2,3,None,3,None,1]
    res = Solution().rob(root)
    print(res)

if __name__ == "__main__":
    main()