from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return res
        dq = deque()
        dq_node = deque()
        dq.append(root)
        dq_node.append(root.val)
        while dq:
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
                dq_node.append(node.left.val)
            else:
                dq_node.append("N")
            if node.right:
                dq.append(node.right)
                dq_node.append(node.right.val)
            else:
                dq_node.append("N")
        while dq_node:
            node = dq_node.popleft()
            res = res + (str(node) if node != "N" else "N") + "|"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        data_list = list(data.split("|"))
        data_list.pop()
        dq = deque()
        dq_node = deque()
        flag = True
        for i in range(len(data_list)):
            if data_list[i] != "N" and data_list[i] != "-":
                if flag:
                    dq.append(TreeNode(int(data_list[i])))
                if not flag:
                    dq.append(TreeNode(-int(data_list[i])))
                    flag = True
            elif data_list[i] == "-":
                flag = False
            else:
                dq.append(None)
        dq_node.append(dq.popleft())
        root = dq_node[0]
        while dq:
            node = dq_node.popleft()
            if node:
                node.left = dq.popleft()
                dq_node.append(node.left)
                node.right = dq.popleft()
                dq_node.append(node.right)
        return root

# Your Coderc object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))