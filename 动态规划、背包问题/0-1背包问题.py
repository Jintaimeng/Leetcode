w = list(map(int, input().split(" ")))#物品重量
v = list(map(int, input().split(" ")))#物品价值
n = len(w)#物品数量
C = int(input())
memo = [[-1 for _ in range(C + 1)] for _ in range(n)]

def knapsack01(w, v, C):
    for j in range(C + 1):#第 0 个物品，放入容量为 j 的包中
        if w[0] <= j:
            memo[0][j] = v[0]
        else:
            memo[0][j] = 0
    for i in range(1, n):
        for j in range(C + 1):
            memo[i % 2][j] = memo[(i-1) % 2][j]
            if w[i] <= j:
                memo[i % 2][j] = max(memo[i % 2][j], v[i] + memo[(i-1) % 2][j - w[i]])
    return memo[(n-1) % 2][C]

if n == 0 or C == 0:
    print(0)
else:
    print(knapsack01(w, v, C))

