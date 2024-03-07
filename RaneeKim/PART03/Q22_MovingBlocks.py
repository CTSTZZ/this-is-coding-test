from collections import deque

def get_next_pos(pos,board) :
    next_pos = [] # 다음 이동할 좌표
    pos = list(pos) # 집합이었던 pos를 list형태로 변환
    
    # 로봇은 두칸을 차지하므로, 1번칸 2번칸에대한 좌표
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4) : 
        # 상하좌우로 이동하는 for문
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        # 이동후의 좌표들이 각각 (두칸이므로 각각) 빈칸일때
        if board[pos1_next_x][pos1_next_y] == 0 and  board[pos2_next_x][pos2_next_y] == 0 :
            # 이동이 가능하다는 뜻이므로 next_pos에 append
            next_pos.append({(pos1_next_x, pos1_next_y) , (pos2_next_x, pos2_next_y)})
        
        # x좌표가 같으면 가로로 놓여져 있음
        '''
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)
        (2,0) (2,1) (2,2) 
        '''
        if pos1_x == pos2_x :
            for i in [-1,1] : # 위쪽 (시계방향 90도) , 아래쪽 (반시계방향 90도)
                # 현재 위치한 좌표에서의 아래 두칸이 모두 0 (i=1 일때)
                # 현재 위치한 좌표에서의 위 두칸이 모두 0 (i=-1일때)
                if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0 :
                    # 회전이 가능하다는 뜻이므로 회전 후 위치하게 될 좌표들을 next_pos에 append
                    # 두개인 이유는 회전축이 될 기준점이 왼쪽일때 오른쪽일때 두개이므로                  
                    next_pos.append({(pos1_x,pos1_y), (pos1_x + i, pos1_y)})
                    next_pos.append({(pos2_x,pos2_y), (pos2_x + i, pos2_y)})
        
        # y좌표가 같으면 세로로 놓여져 있음
        elif pos1_y == pos2_y :
            for i in [-1,1] : # 왼쪽 (시계방향 90도) , 오른쪽 (반시계방향 90도)
                if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0 :
                    next_pos.append({(pos1_x,pos1_y), (pos1_x, pos1_y + i)})
                    next_pos.append({(pos2_x,pos2_y), (pos2_x, pos2_y + i)})
    return next_pos


def solution(board) :
    # 현재 지도를 가져오는데 그 지도의 외각에 벽을 두는 형태로 new_board를 할거임
    '''
        (0,0) (0,1) (0,2) (0,3) (0,4)
        (1,0) (1,1) (1,2) (1,3) (1,4)
        (2,0) (2,1) (2,2) (2,3) (2,4)
        (3,0) (3,1) (3,2) (3,3) (3,4)
        (4,0) (4,1) (4,2) (4,3) (4,4)
        
        진짜로 사용되는 지도는 중간에 위치한 (1,1) ~ (3,3) 의 지도다 
    '''
    n = len(board)
    new_board = [[1]* (n+2) for _ in range(n+2)]

    # 기존 지도를 새로운 지도로 그대로 옮길건데 좌표는 +1을 해두면 된다.
    for i in range(n) :
        for j in range(n) :
            new_board[i+1][j+1] = board[i][j]
    
    q = deque() # dfs를 위해
    visited = [] # 방문된 곳을 저장하는 리스트
    pos = [(1,1),(1,2)]  # 시작위치 설정 -> 이때 집합으로 넣어지므로 get_next_pos함수에서 집합을 list로 변환하는 작업이 필요
                        # [] 으로 고쳐서 하면 'set' object is not subscriptable 에러뜸
    q.append((pos,0)) # 시작좌표와 걸린시간(시작점이므로 0초)를 q에 append                            
    visited.append(pos) # 시작 좌표는 방문한 곳이므로 visited에 append

    while q :
        pos, cost = q.popleft() # 좌표와 시간을 꺼낸다

        if (n,n) in pos : # 현재 좌표가 n,n에 도달했을 경우 걸리시간 return
            return cost
        
        # get_next_pos 함수에 (현재 로봇이 위치한 좌표, 새로운 지도)를 넣어서 불러온다
        # get_next_pos 함수는 로봇이 다음에 가게 될 좌표들로 return된다.

        for next_pos in get_next_pos(pos, new_board) : 
            if next_pos not in visited : # 로봇이 다음으로 가게될 좌표들이 방문된곳이 아니라면
                q.append((next_pos, cost+1)) # q에 가게될 좌표와 현재시간+1초 (1초 지났으므로)을 append 시키고
                visited.append(next_pos) # 가게될 좌표는 방문으로 표시
    return 0
