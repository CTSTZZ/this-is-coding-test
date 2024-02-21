from collections import deque

n,k = map(int,input().split())
graph = []
viruss = []
for i in range(n) :
    graph.append(list(map(int,input().split())))
    
    for j in range(n) :
        if graph[i][j] != 0 :
            viruss.append((graph[i][j],0,i,j))

viruss.sort()
q = deque(viruss)

s,x,y = map(int,input().split())

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q :
    virus, vs, vx, vy = q.popleft()

    if vs == s :
        break

    for i in range(4) :
        nx = vx + dx[i]
        ny = vy + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n :
            if graph[nx][ny] == 0 :
                 graph[nx][ny] = virus
                 q.append((virus, vs+1, nx,ny))

print(graph[x-1][y-1])