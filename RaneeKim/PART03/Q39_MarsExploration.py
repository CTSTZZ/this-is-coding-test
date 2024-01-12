import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [-1,0,1,0] # 위, 오른쪽, 아래, 왼쪽
dy = [0,1,0,-1]

for _ in range(int(input().strip())) :
    n = int(input().strip())

    mars = []
    for _ in range(n) :
        mars.append(list(map(int, input().split())))
    
    distance = [[INF]*n for _ in range(n)] # 2차원으로 생각해야하므로 distance 자체가 2*2표로 만들어짐

    x,y = 0,0 
    q = [(mars[x][y],x,y)]
    distance[x][y] = mars[x][y]

    while q :
        dist, a, b = heapq.heappop(q)
        if distance[a][b] < dist :
            continue
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            cost = dist +  mars[nx][ny]
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
    
    print(distance[n-1][n-1])
