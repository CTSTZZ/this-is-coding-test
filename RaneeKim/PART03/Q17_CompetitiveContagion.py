from collections import deque

n,k = map(int,input().split())
graph = [] # 전체 지도 
viruss = [] # 바이러스가 있는 좌표 리스트
for i in range(n) :
    graph.append(list(map(int,input().split()))) # 전체 지도에 정보를 input
    
    for j in range(n) :
        if graph[i][j] != 0 : # 좌표가 0이 아니라면 = 바이러스가 있다면
            viruss.append((graph[i][j],0,i,j)) # (바이러스숫자, 시간(0,시작시간이닌깐), x좌표,y좌표) 를 append

viruss.sort() # 바이러스숫자로 sort(숫자가 낮은 순서부터 퍼지닌깐)
q = deque(viruss) 

s,x,y = map(int,input().split()) # 시간, s초 지난후 확인할 x좌표, y좌표

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q : # q가 빌때까지 while문 돌리기
    virus, vs, vx, vy = q.popleft()

    if vs == s : # 시간이 s만큼 채워졌으면 break
        break

    for i in range(4) : # 바이러스가 상하좌우로 퍼지므로
        nx = vx + dx[i]
        ny = vy + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n : # 이동한 좌표가 지도안에 있고
            if graph[nx][ny] == 0 : # 빈공간이면
                 graph[nx][ny] = virus # 바이러스가 퍼짐
                 q.append((virus, vs+1, nx,ny)) # 이때의 바이러스숫자와, 시간(1초지났으므로 +1), 현재의 x좌표, y좌표를 q에 append

print(graph[x-1][y-1]) 