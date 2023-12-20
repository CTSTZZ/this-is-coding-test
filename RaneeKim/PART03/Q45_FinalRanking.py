from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input().strip())) :
    n = int(input().strip()) # 노드개수
    indegree = [0] * (n+1) # 진입차수 초기화
    graph = [[False]*(n+1) for _ in range(n+1)] # 각 학생들 순위 정보 초기화
    data = list(map(int,input().split()))
    for i in range(n) :
        for j in range(i+1,n) :
            graph[[data[i]][data[j]]] = True
            indegree[data[j]] += 1

'''
출력조건이 있으므로 들어온 데이터는 data = [5 4 3 2 1] 로 index를 0부터 시작했기 때문에 1~n+1이 아니라 0~n 
graph의 index를 찾아가는 것 -> graph의 index는 실제 학생번호와 같음 1번 학생 index는 1

graph[[data[0]][data[1]]] = graph[[5][4]] = True 5번학생이 4번학생보다 순위가 높으므로 True
graph[[data[0]][data[2]]] = graph[[5][3]] = True
graph[[data[0]][data[3]]] = graph[[5][2]] = True
graph[[data[0]][data[4]]] = graph[[5][1]] = True

graph[[data[1]][data[2]]] = graph[[4][3]] = True
graph[[data[1]][data[3]]] = graph[[4][2]] = True
graph[[data[1]][data[4]]] = graph[[4][1]] = True
.
.
.
행번호(→)의 학생이 열번호(↓)의 학생보다 순위가 높으면 True로 바꾸는 과정 

indegree[data[j]] = indegree[4] += 1  -> [0 0 0 0 1 0] , 4번 학생보다 높은 번호가 몇개있는지 counting

'''


m = int(input().strip()) # 올해 변경된 순위 개수
for i in range(m) :
    a,b = map(int,input().split()) 
    if graph[a][b] : # 만약 a순위가 b순위 보다 높다면 -> if graph[a][b] == True
        graph[a][b] = False # a순위는 b순위보다 낮다로 바꾸고
        graph[b][a] = True # 자연스럽게 b순위는 a순위보다 높다로 바뀜
        indegree[a] += 1 # a순위보다 큰 순위가 하나 더 추가 됐으므로 +1 (b가 더 커졌으므로)
        indegree[b] -= 1 # b순위는 a순위보다 커졌으므로 -1
    else :
        graph[a][b] = True
        graph[b][a] = False
        indegree[a] -= 1
        indegree[b] += 1

result = []
q = deque()

certain = True # 정렬결과가 하나인가 (현재는 하나이므로 True로 초기화)
cycle = False # 그래프 내 사이클이 존재하는가 (현재는 사이클 존재X False로 초기화)

# 첫 시작은 진입차수가 0인 즉, 순위가 제일 큰 학생번호부터 시작
for i in range(1, n+1) :
    if indegree[i] == 0 :
        q.append(i)

for _ in range(n) :
    if len(q) == 0 :
    # q에 아무 원소도 없는것 -> 진입차수가 0인 학생번호가 없다 -> 학생들순위간의 사이클발생 -> 일관성X
        cycle = True
        break
    if len(q) >= 2 :
        certain = False
        break
    
    '''
    q에 원소가 2개 이상인것 -> 서로 순위가 같은 학생번호가 있다는 뜻 
    -> 진짜 같은게 아니라 1번학생 > 2번학생,3번학생 > 4번학생 이런식이므로 정렬결과가 여러개일 수 있다
    ex) 1번 > 2번 > 3번 > 4번 or 1번 > 3번 > 2번 > 4번
    '''

    now = q.popleft()
    result.append(now)
    for j in range(1, n+1) :
        if graph[now][j] :
            indegree[j] -= 1 # now와 j의 순위를 확인했으니 진입차수를 -1
            if indegree[j] == 0 : # 확인할때 j = 0이라는건 j보다 순위가 높은 학생번호는 모두 확인했다는 뜻
                q.append(j) # j의 순위도 확인 궈


if cycle :
    print("IMPOSSIBLE")
elif not certain :
    print("?")
else :
    for i in result :
        print(i, end=' ')
    print()