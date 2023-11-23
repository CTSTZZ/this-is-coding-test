import sys
input = sys.stdin.readline

n = int(input().strip()) # 게임판 길이
k = int(input().strip()) # 사과 몇 개
data = [[0]*(n+1) for _ in range(n+1)] # 게임판 2x2 그래프
info = []

# 사과의 좌표 받기
for _ in range(k) :
    a,b = map(int, input().split()) 
    data[a][b] = 1

# 뱀 이동 받기
l = int(input().strip()) 
for _ in range(l) : 
    x,c = input().split()
    info.append((int(x),c)) 

# 동,남,서,북
dx = [0,1,0,-1]  
dy = [1,0,-1,0]

def turn(direction,c) :
    if c == "L" :
        direction = (direction-1) % 4
    else :
        direction = (direction+1) % 4
    return direction

def snake() :
    x,y = 1,1 # 현재 1,1에 위치하고 있다
    data[x][y] = 2 # 위치하고 있는 칸은 2로 바꿔줌
    direction = 0 # 시작값은 0 (오른쪽방향으로 보고있음)
    time = 0
    index = 0
    q = [(x,y)] # 뱀이 위치하고 있는 칸 좌표를 q리스트에 어펜드

    while True :

        # 현재값에서 방향에 맞춰 움직여라
        nx = x + dx[direction] 
        ny = y + dy[direction]

        # 게임판에서 벗어나지 않고, 자기 자신과 부딪히지 않으면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2 :
            # 움직인칸에 사과가 없을 때
            if data[nx][ny] == 0 :
                data[nx][ny] = 2 # 뱀이 움직였으므로 뱀이 위치한 칸을 2로 바꿈
                q.append((nx,ny)) # 위치하고 있는 칸 좌표를 q리스트에 append
                px,py = q.pop(0) 
                data[px][py] = 0 # 사과가 없으므로 꼬리가 위치했던 칸의 좌표는 0으로 바꾸고 q리스트에서도 삭제
            
            # 움직인칸에 사과가 있을 때
            if data[nx][ny] == 1 :
                data[nx][ny] = 2
                q.append((nx,ny)) # 사과가 없을때와 동일하지만 꼬리칸의 좌표를 2로 살려둠
        
        # 게임판에서 벗어나거나, 자기 자신과 부딪힐 때 시간은 흘렀으니 1초 누적 후 break
        else :
            time += 1 
            break
        
        x,y = nx, ny # 현재값을 이동한 값으로 치환
        time += 1  # 시간 지났으닌깐 1초 누적

        # 만약에 index값이 뱀이 이동을 시도했던 값(l) 보다 작고 time값이 뱀이 이동할 수 있는 시간과 같아진다면
        # info = [ (3,D) , (15,L) , (17,D) ]
        if index < l and time == info[index][0] : 
            direction = turn(direction, info[index][1])
            index += 1 # 다음 이동을 실행하라
    
    return time # 시간을 반환

print(snake())