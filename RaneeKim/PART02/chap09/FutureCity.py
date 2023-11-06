# 1->x, x->k 까지 가는 for문을 만들려고함
# but 각자의 노선만큼 for문의 갯수가 필요한데 통일이 안됨
# ex) 1 -> 4 -> 5 -> 2 의 노선이면 2까지이면 1->4, 4->5, 5->2 세번 , 5까지면  1->4, 4->5 등 기준이 없어 for문을 몇번 써야할지 확실하지 않음

import sys
input = sys.stdin.readline


INF = int(1e9)

n,m = map(int, input().split()) # 11,15

graph = [[INF]* (n+1) for _ in range(n+1)] # 2차원 그래프(표라고 생각하고) 표를 (n+1)*(n+1) 만들어서 무한으로 리셋
                                            # n+1인 이유는 입력받을 n이 1이상이기 때문 (파이썬은 리스트는 0이 시작이라는 점)
                                            # -> 1행1열 즉 graph[0][n+1]~grahp[n+1][0] 은 버리는 줄

for a in range(1, n+1) : # 위의 이유와 동일 1~(n+1)인 이유
    for b in range(1, n+1) : 
        if a == b:
            graph[a][b] = 0 # 자기 경로는 0으로 셋팅 ex) 1->1, 2->2 등

for _ in range(m) :
    a,b = map(int, input().split()) # 연결되어있는 노선 입력받기
    graph[a][b] = 1 # 연결된 노선은 1로 셋팅 
    graph[b][a] = 1

x, k = map(int, input().split()) # 

for i in range(1, n+1) : # 책에는 i대신 k라고 적혀져있어서 입력받은 k와 혼돈되어 i로 고침
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
            # 삼중을 하는 이유 : 모든 노선을 확인하기 때문 
            # 이해안되었던 부분 : 4개의 노선을 거쳐서 가면 삼중으로 될까? 
            # -> 결국 다이나믹프로그래밍과 같은 몇개의 노선을 거치든 그 전에 지났던 노선들은 저장이 되어있음 (count되어있다고 보면됨)

distance = graph[1][x] + graph[x][k]
print(distance)
