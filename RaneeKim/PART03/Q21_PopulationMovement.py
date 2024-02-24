from collections import deque

# 땅크기, 최소, 최대
n,l,r = map(int,input().split()) 

graph = [] # 땅 정보 (도시정보)
for _ in range(n) :
    graph.append(list(map(int,input().split())))

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def process(x,y,index) : # 해당나라의 좌표와 index를 받는 함수
    united = [] 
    united.append((x,y)) # 연결된 연합 정보를 닮기위한 리스트

    q = deque()
    q.append((x,y)) 
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 인구 누적 더하기
    count = 1 # 현재 연합에 들어가 있는 국가의 수

    while q :
        x,y = q.popleft()

        for i in range(4) : # 현재 위치에서 4방향
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1 : # 좌표가 땅안에 있고, 확인되지 않은 국가라면
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r : # 그 차이가 최소값과 최대값을 만족한다면
                    q.append((nx,ny)) # q에 append

                    union[nx][ny] = index # 현재 위치한 나라도 해당 연합에 추가됨
                    summary += graph[nx][ny] # 인구누적 더하기
                    count +=1  # 연합이 한 나라 늘었으닌깐 +1
                    united.append((nx,ny)) # 연합에 해당 나라가 추가됨
    
    for i,j in united : # 모든 연합들의 추가가 끝나면 인구 균등하게 나누기
        graph[i][j] = int(summary/count)
    return count

date = 0 # 연합이 시작된 날짜를 카운트위해 0으로 초기화

while True :
    union = [[-1]*n for _ in range(n)] # 모든 나라가 연합 전이므로 -1로 초기화
    index = 0 # 연합 번호도 0으로 초기화
    for i in range(n) :
        for j in range(n) :
            if union == -1 : # 나라가 연합 전이라면
                process(i,j,index) 
                index += 1
   
    if index == n*n : # 만약 연합이 하나도 이루어지지않았을때 이중for문은 n*n 번 돌아가므로 index가 n*n이 될것이다. 
        break # 이때, date는 추가되지않고 while문이 끝나야 하므로 break문을 사용
    
    date += 1 # 한번으로 하루 연합이 끝났으니 +1

print(date)