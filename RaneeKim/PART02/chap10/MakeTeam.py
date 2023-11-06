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
