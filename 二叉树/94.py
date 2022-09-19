class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderResult = []
        stack = list()
        node = root
        nodeLeft = 100
        nodeRight = 200
        nodeUp = 300
        nodeState = nodeLeft
        while node:
            if nodeState == nodeLeft:
                if node.left:
                    stack.append(node)
                    node = node.left
                else:
                    nodeState = nodeRight
            elif nodeState == nodeRight:
                inorderResult.append(node.val)
                if node.right:
                    stack.append(node)
                    node = node.right
                    nodeState = nodeLeft
                else:
                    nodeState = nodeUp
            elif nodeState == nodeUp:
                parent = None
                if stack:
                    parent = stack.pop()
                    if parent.left == node:
                        nodeState = nodeRight
                node = parent
        return inorderResult