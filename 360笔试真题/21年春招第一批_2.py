N, M, K = map(int, input().split(" "))
kmList = []
money = []
for i in range(N):
    temp1, temp2 = map(int, input().split(" "))
    kmList.append(temp1)
    money.append(temp2)
memo = [[0 for _ in range(2)] for _ in range(N)]
memo[N - 1][0] = money[N - 1]
memo[N - 1][1] = K

for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if kmList[j] - kmList[i] <= M:
            if memo[i][0] <= memo[j][0] + money[i] and memo[j][1] > 0:
                memo[i][0] = memo[j][0] + money[i]
                memo[i][1] = memo[j][1] - 1

print(memo[0][0])
