from collections import deque

n,m,k,x = map(int,input().split())
maps = [ [] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int, input().split())
    maps[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

# [[], [2, 3], [3, 4], [], []]
# [-1, 0, -1, -1, -1]

q = deque()
q.append(x)

while q :
    a = q.popleft()
    b = distance[a]

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



