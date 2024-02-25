from itertools import combinations

n = int(input()) # 방 크기 (세로=가로) 
board = [] # 방 정보
teachers = [] # 선생님이 있는 곳 좌표 
spaces = [] # 빈 공간 좌표

for i in range(n) : # 방 크기의 길이 만큼 for문
    board.append(list(input().split())) # 방 정보를 입력받아서 방의 가로(list형=n행들)
    for j in range(n) :
        if board[i][j] == 'T' : # 선생님이 있으면
            teachers.append((i,j)) # teachers 리스트에 append
        if board[i][j] == 'X' :
            spaces.append((i,j)) # 선생님과 학생외 빈 공간은 spaces 리스트에 append
'''
[['X', 'S', 'X', 'X', 'T'],
 ['T', 'X', 'S', 'X', 'X'], 
 ['X', 'X', 'X', 'X', 'X'],
 ['X', 'T', 'X', 'X', 'X'], 
 ['X', 'X', 'T', 'X', 'X']]
 
# [(0, 4), (1, 0), (3, 1), (4, 2)]
# [(0, 0), (0, 2), (0, 3), (1, 1), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 3), (4, 4)]  
'''


'''
3X3

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)


'''
def watch(x,y,direction) : # x좌표, y좌표, 방향 (좌:0  우:1  상:2  하:3)
    
    if direction == 0 : 
        while y >= 0 : # 계속 왼쪽 갈 예정 -> 방의 제일 왼쪽 좌표는 (x,0) 이므로 y가 0 이상일때 까지 while문 돌리기
            if board[x][y] == 'S' :  # 학생 발견하면 True로 치환
                return True
            if board[x][y] == 'O' : # 장애물 발견하면 False로 치환
                return False
            y -= 1
                    
    if direction == 1 : # 계속 오른쪽 으로 갈 예정 -> 방의 제일 오른쪽 좌표는 (x,n-1) 이므로 y가 n미만일때 까지 while문 돌리기
        while y < n :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            y += 1
    
    if direction == 2 : # 계속 위로 갈 예정 -> 방의 제일 위 좌표는 (0,y) 이므로 x가 0이상일때 까지 while문 돌리기
        while x >= 0 :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            x -= 1

    if direction == 3 : # 계속 밑으로 갈 예정 -> 방의 제일 위 좌표는 (n-1,y) 이므로 x가 n미만일때 까지 while문 돌리기
        while x < n :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            x += 1
    
    return False

# 장애물 설치 후 학생이 감지되는지 확인하는 함수
def process() :
    
    for x,y in teachers : # 각 선생님들의 좌표를 x,y로 받고
        for i in range(4) : # 각 선생님마다 상상상상, 하하하하하하... , 좌좌조ㅏ좌좌좌좌... ,  우우우우우ㅜ우우.. 확인
            if watch(x,y,i) : 
                return True # 학생을 발견한다면 True로 치환
    return False 



find = False

for data in combinations(spaces,3) : # 빈 공간의 좌표를 3개씩 묶어주어 나올 수 있는 모든 경우를 조합을 사용하여 만들었음
    
    for x,y in data :
        board[x][y] = 'O' # 뽑은 3개의 좌표에 장애물 설치

    if not process() : # process 함수가 True가 아니라면, 즉 학생을 발견하지 못했다면
        find = True # find는 True
        break # 이미 원하는 답을 얻었으니 다른 조합을 확인할 필요없으므로 break를 사용하여 'for data in combinations(spaces,3)'문을 종료
    
    for x,y in data : # 다음 조합도 확인해야하므로 설치된 장애물을 다시 삭제
        board[x][y] = 'X' 


if find : 
    print('True')
else : 
    print('No')
    