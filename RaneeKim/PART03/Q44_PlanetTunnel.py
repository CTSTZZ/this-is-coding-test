import sys
input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union(parent,a,b) :
    a = parent[a]
    b = parent[b]
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input().strip())

planet = []
for _ in range(n) :
    a,b,c = map(int, input().split())
    planet.append((a,b,c))

data = []
for i in range(n) :
    for j in range(n) :
        if i != j :
            a = planet[i]
            b = planet[j]
            result = min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))
            data.append((i,j,result))

data.sort(key=lambda x:x[2])
parent = []
for i in range(n) :
    parent.append(i)

cost = 0
for i in data :
    if find_parent(parent,i[0]) != find_parent(parent,i[1]) :
        union(parent,i[0],i[1])
        cost += i[2]

print(cost)