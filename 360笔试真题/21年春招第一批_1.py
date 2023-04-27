n = int(input())
aList = list(map(int, input().split(" ")))
sum = sum(aList)
for i in range(len(aList)-1):
    for j in range(i+1, len(aList)):
        sum += aList[i] | aList[j]
print(sum)

balls = int(input().strip())
data = list(map(int, input().strip().split()))
res = sum(data)
for i in range(32):
    temp = 0
    for c in data:
        if (c >> i) & 1 == 1:
            temp += 1
            if temp <= 1:
                res += 2 ** i * (temp * (balls - temp))
            else:
                res += 2 ** i * (temp * (balls - temp) + (temp * (temp - 1)) / 2)
print(int(res))