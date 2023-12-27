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
    
    return print(cost[1:])

for i in range(1,n+1) :
    solution(i)


