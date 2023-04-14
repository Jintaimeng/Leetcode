from queue import Queue
from collections import defaultdict


def bfs(root, tree):
    queue = Queue()
    queue.put(root)
    children = [root]
    while not queue.empty():
        cur = queue.get()
        if cur in tree:
            # 还没到叶子节点
            for child in tree[cur]:
                queue.put(child)
                children.append(child)
    return children


def modify(root):
    if tree[root]:
        for child in tree[root]:
            # 将子节点指向父节点的关系删除
            tree[child].remove(root)
            modify(child)


if __name__ == "__main__":
    n = int(input())
    tree = defaultdict(lambda: [])
    for _ in range(n - 1):
        x, y = map(int, input().strip().split())
        tree[x].append(y)
        tree[y].append(x)
    # 根据拓扑关系，将树改为有向图
    modify(1)
    colors = tuple(map(int, input().strip().split()))
    q = int(input())
    for _ in range(q):
        t = int(input())
        # bfs获得节点t的所有子节点(包括自己)
        children = bfs(t, tree)
        # 颜色计数器
        counter = defaultdict(lambda: 0)
        for child in children:
            counter[colors[child - 1]] += 1
        # 输出数量最多的颜色
        maxColor = 5001
        maxCount = 0
        for color in counter:
            if maxCount < counter[color]:
                maxCount = counter[color]
                maxColor = color
            elif maxCount == counter[color]:
                maxColor = min(color, maxColor)
        print(maxColor)