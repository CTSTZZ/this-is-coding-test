import sys

input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x :
        find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b) :
    a = parent[a]
    b =parent[b] 
    if a<b :
        parent[b] = a
    else :
        parent[a] = b


trip = []
n,m = map(int,input().split())

for _ in range(n) :
    data = list(map(int,input().split()))
    trip.append(data)

city1,city2,city3,city4 = map(int,input().split())

cheak = []
for i in range(n) :
    for j in range(n) :
        if trip[i][j] == 1 :
            cheak.append((i+1,j+1))

parent = []
for i in range(n+1) :
    parent.append(i)

for c in cheak :
    a = c[0]
    b= c[1]
    union(parent,a,b)

if find_parent(parent,city1) == find_parent(parent,city2) == find_parent(parent,city3) == find_parent(parent,city4) :
    print('YES')
else :
    print('NO')
 