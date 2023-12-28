import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    i,a,b = map(int, input().split())
    graph[i].append((a,b))

def solution(city) :
    cost = [100000] * (n+1) # 최단비용 세팅
    
    cost[city] = 0
    
    q = []
    heapq.heappush(q, (0,city))    

    while q :
        won, now = heapq.heappop(q)
        if cost[now] < won :
            continue
        for i in graph[now] :
            won = cost[now] + i[1]
            if won < cost[i[0]] :
                cost[i[0]] = won
                heapq.heappush(q,(won,i[0]))
    for i in range(len(cost)) :
        if cost[i] == 100000 :
            cost[i] = 0
    
    return cost[1:]

for i in range(1,n+1) :
    a = solution(i)
    for e in a :
        print(e, end = " ")
    print()



'''
n = int(input().strip())
m = int(input().strip())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1) :
    for b in range(1,n+1) :
        if a == b :
            graph[a][b] = 0

for _ in range(m) :
    a,b,cost = map(int, input().split())
    if cost < graph[a][b] :
        graph[a][b] = cost

for i in range(1,n+1) :
    for a in range(1,n+1) :
        for b in range(1,n+1) :
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

for a in range(1,n+1) :
    for b in range(1,n+1) :
        if graph[a][b] == INF :
            graph[a][b] = 0
        print(graph[a][b], end=" ")
    print()
    
'''
