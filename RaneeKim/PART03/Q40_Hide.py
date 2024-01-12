import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
hide = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
    a,b = map(int, input().split())
    hide[a].append((b,1))
    hide[b].append((a,1))

def dijkstra() :
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in hide[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

maxdist = dijkstra()
result = []
for i in range(len(maxdist)) :
    if maxdist[i] == max(maxdist[1:]) :
        result.append(i)

print(min(result),max(maxdist[1:]),len(result))
