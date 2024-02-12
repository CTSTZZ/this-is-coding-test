from collections import deque

# 도시개수, 도로개수, 거리정보, 출발도시
n,m,k,x = map(int,input().split())

maps = [ [] for _ in range(n+1)] # N+1 -> 도시번호와 INDEX맞추려고
for _ in range(m) :
    a,b = map(int, input().split())
    maps[a].append(b)

distance = [-1] * (n+1) # 자기자신은 0으로 초기화시켜야하므로
distance[x] = 0 

# [[], [2, 3], [3, 4], [], []]
# [-1, 0, -1, -1, -1] -> [-1,0,1,1,2]

q = deque()
q.append(x)

while q :
    a = q.popleft() # 현재 서있는 시티
    b = distance[a] # 현재시티까지의 거리

    for next_node in maps[a] :
        if distance[next_node] == -1 :
            distance[next_node] = b + 1
            q.append(next_node)

count = 0
for i in range(n+1) :
    if distance[i] == k :
        print(i)
        count += 1
if count == 0 :
    print(-1)



