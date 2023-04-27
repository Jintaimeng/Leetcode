N, M, K = map(int, input().split(" "))
kmList = []
money = []
for i in range(N):
    temp1, temp2 = map(int, input().split(" "))
    kmList.append(temp1)
    money.append(temp2)
memo = [0] * (K + 1)
memo[0] = money[0]
location = 0
for k in range(1, K + 1):
    nowMax = -1
    nextIndex = location
    for i in range(location + 1, M):
        if kmList[i] - kmList[location] <= M and money[i] > nowMax:
            nowMax = money[i]
            nextIndex = i
        else:
            break
    memo[k] = nowMax + memo[k-1]
print(memo[K-1])
