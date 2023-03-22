n, x, y = input().split(" ")
n, x, y = int(n), int(x), int(y)
an = [int(a) for a in input().split(" ")]
res = []
an.sort()
for i in range(x, y+1):
    if n-i >= x and n-i <= y:
        res.append(an[i-1])
print(sorted(res)[0])