import sys
input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())

parent = []
for i in range(n) :
    parent.append(i)

data = []
for _ in range(m) :
    a,b,c = (map(int,input().split()))
    data.append((a,b,c))

data.sort(key=lambda x:x[2])
cheak = 0
all_sum = 0
for d in data :
    print(d,d[0],d[1],d[2])
    all_sum += d[2]
    if find_parent(parent,d[0]) != find_parent(parent,d[1]) :
        union(parent,d[0],d[1])
        cheak += d[2]
        print(parent)

print(all_sum-cheak)

