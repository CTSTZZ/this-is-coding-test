import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# n,m,start = map(int, input().split()) 

n = 6  # n은 노드 개수
m = 10  # m은 간선 개수
start = 1 # start는 시작 노드


distance = [INF] * (n+1) # start로부터 다른 노드까지 distance(최단거리테이블)는 무한으로 세팅

'''
graph = [[] for i in range(n+1)]
for _ in range(m) :
    x,y,z= map(int, input().split())
    graph[x].append((y,z)) 
'''
graph = [ [], [(2,2),(3,5),(4,1)] , [(3,2),(4,2)] , [(2,3)] , [(3,3),(5,1)] , [(3,1)] , [(3,3)] ] 

'''
graph[0] 
graph[1] 1->2 (2시간) , 1->3 (5시간) , 1->4 (1시간)
graph[2] 2->3 (2시간) , 2->4 (2시간)
graph[3] 3->2 (3시간)
graph[4] 4->3 (2시간) , 4->5 (1시간)
graph[5] 5->3 (1시간) 
graph[6] 6->3 (3시간)
'''

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0,start)) # 시작 노드로 가기 위한 최단 경로는 0으로 세팅하고 큐에 삽입  
                                 # q = [ (0,1) ]
    
    distance[start] = 0  # 시작노드 -> 시작노드는 최단경로가 0이므로
    
    while q : # 큐가 비어질 때 까지 while문 돌리기
        dist, now = heapq.heappop(q) # dist와 now는 큐에서 첫번째 즉, 최단 거리가 짧은 노드에 대한 정보 꺼내기
        
        if distance[now] < dist : # 이미 처리된 노드라면 무시
            continue
        for i in graph[now] : # 현재노드와 연결된 다른 노드들 확인
            cost = dist + i[1] # 현재 노드를 거쳐서 다른 노드로 이동하는 경우
            if cost < distance[i[0]] : # 그 경우가 start와 다른 노드로 이동하는 경우 보다 짧을 때
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0])) # 
    
dijkstra(start)

count = 0

max_distance = 0
for d in distance : # start에서 다른 노드로 가는 최단 경로 시간 숫자 확인 
    if d != INF : 
        count += 1 # 최단경로 즉, 가는 길이 있을 때마다 +1
        max_distance = max(max_distance, d) # 걸린 시간은 최단 경로들 중 max 값


'''
n,m,c = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

find_max = []
for _ in range(m) :
    x,y,z = map(int, input().split())
    graph [x][y] = z
    find_max.append(z)
fm = max(find_max)

def solution(n,c) :
    global fm
    global graph
    letter = []
    for i in range(n+1) :
        if graph[c][i] <= fm :
            letter.append([i,graph[c][i]])
    count = len(letter)
    length = max([letter[i][1] for i in range(count)])
    return print(count , length)

solution(n,c)
'''