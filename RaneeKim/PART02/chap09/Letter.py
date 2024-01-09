import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split()) # n은 노드 개수, m은 간선 개수, start는 시작 노드

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) # distance는 무한으로 세팅

for _ in range(m) :
    x,y,z= map(int, input().split())
    graph[x].append((y,z)) 

'''
graph = [ [ ] , [(2,2),(3,4)] , [(5,3)] , [ ] , [(2,5)] , [ ] ] 
graph[0] 
graph[1] 1->2 (2시간) , 1->3 (4시간)
graph[2] 2->5 (3시간)
graph[3] 
graph[4] 4->2 (5시간)
graph[5]
'''

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0,start))



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