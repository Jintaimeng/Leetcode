#Leetcode上报内部错误
#非递归方法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Command:
    def __init__(self, s, node):
        self.s = s
        self.node = node
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = deque()
        n = Command("go", root)
        stack.append(n)
        while len(stack) > 0:
            command = stack.pop()
            if command.s == "print":
                res.append(command.node)
            elif command.s == "go":
                if command.node.right is not None:
                    node_right = Command("go", command.node.right)
                    stack.append(node_right)
                if command.node.left is not None:
                    node_left = Command("go", command.node.left)
                    stack.append(node_left)
                stack.append(Command("print",command.node))
        return res

