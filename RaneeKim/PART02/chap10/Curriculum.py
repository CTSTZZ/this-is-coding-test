import sys
input = sys.stdin.readline

n = int(input().strip())
curriculum = [[]] # 첫번째리스트 즉 curriculum[0] 은 비어있어야하므로 초기화를 이렇게 시킴
time = [0] * (n+1)

for i in range(n) :
    data = list(map(int,input().split()))
    time[i+1] = data[0]
    curriculum.append(data[1:-1]) 
    # [ [] , [] , [1] , [1] , [3,1] , [3] ]

for i in range(len(curriculum)) :
    if len(curriculum[i]) == 0 :
        continue
    else :
        max_l = time[curriculum[i][0]]
        for l in curriculum[i] :
            if max_l <= time[l] :
                max_l = time[l]
        time[i] = time[i] + max_l

for i in time[1:] :
    print(i)