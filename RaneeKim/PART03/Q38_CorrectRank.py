import sys

input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
rank_g = [ [INF]*(n+1) for _ in range(n+1) ]

for a in range(1,n+1) :
    for b in range(1,n+1) :
        if a == b :
            rank_g[a][b] = 0

for _ in range(m) :
    a,b = map(int, input().split())
    rank_g[a][b] = 1

for k in range(1,n+1) :
    for a in range(1,n+1) :
        for b in range(1, n+1) :
            rank_g[a][b] = min(rank_g[a][b] , rank_g[a][k]+rank_g[k][b])

result = 0
for i in range(1,n+1) :
    count = 0
    for j in range(1,n+1) :
        if rank_g[i][j] != INF or rank_g[j][i] != INF :
            count += 1
    if count == n :
        result += 1

print(result)