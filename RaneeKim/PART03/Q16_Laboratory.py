n,m = map(int,input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n) :
    data.append(list(map(int,input().split())))

# 위,오른,아래,왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

 # 바이러스가 퍼지는 함수
def virus(x,y) :
    for i in range(4) : # 상하좌우로 다 퍼진다
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m : 
            if temp[nx][ny] == 0 : # 현재 위치가 좌표안에 있고, 빈칸(0)이라면
                temp[nx][ny] = 2 # 바이러스에 전염
                virus(nx,ny)

def get_score() :
    score = 0
    for i in range(n) : # 연구소를 모두 확인했을때,
        for j in range(m) :
            if temp[i][j] == 0 : # 빈칸의 개수만큼 점수가 올라감
                score += 1
    return score

def solution(count) : # 완전탐색 -> 3개의 벽을 세울 수 있는 모든 경우를 생각하여 빈칸이 max가 되는 부분을 찾는다.

    global result

    if count == 3 : # 벽의 개수가 3개가 되었을 때,
        for i in range(n) :
            for j in range(m) : 
                temp[i][j] = data[i][j] # temp의 리스트를 임의로 벽이 세워진 연구소 (data) 리스트로 복사
        
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2 : # temp에서 바이러스가 있는 부분이 발견 되면
                    virus(i,j) # 앞에 정의해둔 virus함수를 불러와서 빈 공간에 바이러스를 전염

        # 정의된 result값과 (초기화일때는 0, 과정이 몇번진행 되었으면 그전 단계에서 구해진 result값)
        # 현재 get_score 함수로 얻어진 빈칸의 공간 중 비교하여 더 큰값을 result값으로 치환
        result = max(result,get_score()) 
        return
    
     # count 3 미만일때, 즉 벽이 세워지는 과정을 설명
    for i in range(n) : 
        for j in range(m) :
            if data[i][j] == 0 : # 빈공간이라면
                data[i][j] = 1 # 일단 벽을 세우고
                count += 1 # conunt 증가
                solution(count) # 재귀함수를 통해서 또 벽을 세움 (2번 재귀함수를 불러오겠죵?)
                data[i][j] = 0 # 임의로 세운 벽들 다 제거 (다음 임의의 벽3개 과정을 위해)
                count -= 1 # count도 다시 0으로 초기화 해야함 (다음 임의의 벽3개 과정을 위해)

solution(0)
print(result)


