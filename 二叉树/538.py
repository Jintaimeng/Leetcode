class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        nodes.sort(reverse=True)
        sum = 0
        map = {}
        for i in range(len(nodes)):
            map[nodes[i]] = nodes[i] + sum
            sum += nodes[i]
        stack.append(root)
        while stack:
            node = stack.pop()
            node.val = map[node.val]
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
