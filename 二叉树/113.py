class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targerSum: int) -> List[List[int]]:
        self.res = []
        self.targetSum = targerSum
        stack = deque()
        self.search(root, 0, stack)
        return self.res
    def search(self, node, value, stack):
        if not node:
            return
        stack.append(node.val)
        value += node.val
        if not node.left and not node.right and value == self.targetSum:
            self.res.append(list(stack))
        self.search(node.left, value, stack)
        self.search(node.right, value, stack)
        value -= node.val
        stack.pop()