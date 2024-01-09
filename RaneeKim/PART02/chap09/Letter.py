import sys
input = sys.stdin.readline

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
