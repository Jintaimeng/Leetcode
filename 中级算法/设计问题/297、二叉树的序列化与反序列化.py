# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        res = ""
        p = root
        while p.left is None and p.right is None:
            if p.right:
                p = p.right
            elif p.left:
                p = p.left
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node == "":
                res = res + "+"
                dq.append("")
                dq.append("")
            else:
                res = res + str(node.val) + "+"
                if node == p:
                    break
                if node.left:
                    dq.append(node.left)
                else:
                    dq.append("")
                if node.right:
                    dq.append(node.right)
                else:
                    dq.append("")
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        data_list = data.split("+")
        dq = deque()
        for i in range(len(data_list) - 1, 2):
            if data_list[0] == "":
                node = None
            else:
                node = TreeNode(int(data_list[0]))
            dq.append(node)
        root = dq.popleft()
        p = root
        while dq:
            if p is not None:
                p.left = dq[0]
                p.right = dq[1]
            node = dq.popleft()
            p = node
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# def main():
#     root =
#     res = Codec().deserialize(Codec().serialize(root))
#     print(res)
#
#
# if __name__ == "__main__":
#     main()