import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1) :
    for b in range(1,n+1) :
        if a == b :
            graph[a][b] = 0

for _ in range(m) :
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split()) 

count = 0

def cheak_num(cheak_list, graph, k) : # 1-> k -> x (k=5, x=4) # 1-> 3 -> 5 -> 4
    global count
    global n
    num_cheak = [] 
    for i in range(1,n+1) :
        for e in cheak_list : # [x]  graph[4][1~5] 연결노드가 있는 애들을 
            if graph[e][i] == 1 :
                num_cheak.append(i) 
    
    if k not in num_cheak : 
        count += 1
        if count < m :
            return(cheak_num(num_cheak,graph,k))
        else :
            return -1
    
    else :
        count += 1
        return count

cheak_num([x],graph,k)
print(cheak_num([k],graph,1))