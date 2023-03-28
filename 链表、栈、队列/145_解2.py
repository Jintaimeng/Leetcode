#非递归方法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = deque()
        stack.append(("go", root))
        while stack:
            command = stack.pop()
            if command[0] == "print":
                res.append(command[1].val)
            elif command[0] == "go":
                stack.append(("print", command[1]))
                if command[1].right:
                    stack.append(("go", command[1].right))
                if command[1].left:
                    stack.append(("go", command[1].left))
        return res