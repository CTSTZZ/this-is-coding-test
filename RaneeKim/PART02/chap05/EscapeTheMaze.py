# bfs 왜 쓰는걸까...? 가장 가까운 길을 찾기 위해서....? 음료 얼려먹기는 모든 길을 가야함

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maze_map = []
for _ in range(n) :
    maze_map.append(list(map(int,input())))  # m을 for문, split()으로 받지않은 이유 : 입력예시때문

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def maze(x,y) :
    
    queue = deque() 
    queue.append((x,y)) # x,y를 큐에 넣는

    while queue :
        x,y = queue.popleft() # 큐에서 첫번째 데이터를(x,y) 꺼내는 함수

        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue # for문에서 위 식을 만족하면 무시해라 <-> break는 위 식을 만족하면 for문을 끝내라
            if maze_map[nx][ny] == 0 :
                continue
            if maze_map[nx][ny] == 1 : # 해당노드를 처음 가는 경우에는 
                maze_map[nx][ny] = maze_map[x][y] + 1 # +1을 더해라
                queue.append((nx,ny))  # 큐에 해당 좌표를 넣어줘라
                # 여기가 이해안가 어떻게 최소값을 반환하는거지 얘는....? -> 캡쳐본으로 설명
        
    return maze_map[n-1][m-1]



