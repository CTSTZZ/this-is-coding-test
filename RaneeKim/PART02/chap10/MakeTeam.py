import sys
input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

'''
parent 
노드번호 0 1 2 3 4 5 6 
부모노드   1 2 3 4 5 6
'''

def union(parent,a,b) :
    a = find_parent(parent,a) 
    b = find_parent(parent,b)
    if a < b : # 부모노드 (a,b =parent[n]이므로)를 기준으로 숫자가 작은걸 기준으로 바뀜
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())

parent = []
for i in range(n+1) :
    parent.append(i) # 부모노드를 자신의 노드번호로 초기화

for _ in range(m) :
    cheak, a,b = map(int,input().split())
    if cheak == 0 :
        union(parent,a,b)
    elif cheak == 1 :
        if find_parent(parent,a) == find_parent(parent,b) :
            print("YES")
        else : 
            print("NO")

'''
1회차
n,m = map(int, input().split())

standard = [0] * (n+1)

for i in range(1,m+1) :
    a,b,c = map(int, input().split())

    if a == 0 : 
        B = standard[b] # for문이 돌아갈때마다 standard[b]값이 바뀌므로 기준이 되는 상수는 for문밖에 있어야함
        C = standard[c]
        for u in range(len(standard)) :
            if standard[u] != 0 :
                if standard[u] == B or standard[u] == C :
                    standard[u] = i        
        standard[b] = standard[c] = i # for문에서 바껴서 없애려고 했으나, 첫번째 0 -> i로 바뀔때 필요해서 걍 놔둠
        print(standard)

    if a == 1 :
        if standard[b] == standard[c] :
            print('YES')
        else :
            print('NO')
'''