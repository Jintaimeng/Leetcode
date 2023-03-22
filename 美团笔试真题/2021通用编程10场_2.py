n = int(input())
nlist = [int(l) for l in input().split(" ")]
nlist.sort()
res = 0
for i in range(1, n + 1):
    res += abs(nlist[i-1] - i)
print(res)