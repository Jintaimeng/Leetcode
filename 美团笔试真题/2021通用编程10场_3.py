#10/12 组用例通过
import heapq

T = int(input())
for t in range(T):
    N = int(input())
    nlist = [int(n) for n in input()]
    M = int(input())
    sex = [s for s in input()]

    res = [] * M
    pq0 = []
    pq1 = []
    for i in range(len(nlist)):
        if nlist[i] == 0:
            heapq.heappush(pq0, i)
        elif nlist[i] == 1:
            heapq.heappush(pq1, i)
    for m in range(M):
        if sex[m] == "M":
            if not len(pq1) == 0:
                res.insert(m, heapq.heappop(pq1)+1)
            else:
                s = heapq.heappop(pq0)
                res.insert(m, s+1)
                heapq.heappush(pq1, s)
        elif sex[m] == "F":
            if not len(pq0) == 0:
                s = heapq.heappop(pq0)
                res.insert(m, s+1)
                heapq.heappush(pq1, s)
            else:
                res.insert(m, heapq.heappop(pq1)+1)
    for r in res:
        print(r)
