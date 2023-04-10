w = list(map(int, input().split(" ")))#物品重量
v = list(map(int, input().split(" ")))#物品价值
n = len(w)#物品数量
C = int(input())
memo = [[-1 for _ in range(n)] for _ in range(C + 1)]

def knapsack01(w, v, C):
    for j in range(C + 1):#第 0 个物品，放入容量为 j 的包中
        memo[0][j] = v[0] if w[0] <= j else 0
    for i in range(1, n):
        for j in range(C + 1):
            memo[i][j] = memo[i-1][j]
            if w[i] <= j:
                memo[i][j] = max(memo[i][j], v[i] + memo[i-1][j - w[i]])
    return memo[n-1][C]

