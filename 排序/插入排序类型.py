n = int(input())
dict = []
for i in range(n):
    s, xi = input().split(" ")
    s = str(s)
    xi = int(xi)
    dict.append((xi, s))
for i in range(1, n):
    now = dict[i]
    j = i
    while j > 0 and now[0] > dict[j-1][0]:
        dict[j] = dict[j - 1]
        j -= 1
    dict[j] = now
for i in range(n):
    print(dict[i][1])