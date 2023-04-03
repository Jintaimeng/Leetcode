from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        node_dq = deque()
        path_dq = deque()
        node_dq.append(root)
        path_dq.append(str(root.val))
        while node_dq:
            node = node_dq.popleft()
            path = path_dq.popleft()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                node_dq.append(node.left)
                new_path = path + "->" + str(node.left.val)
                path_dq.append(new_path)
            if node.right:
                node_dq.append(node.right)
                new_path = path + "->" + str(node.right.val)
                path_dq.append(new_path)
        return res