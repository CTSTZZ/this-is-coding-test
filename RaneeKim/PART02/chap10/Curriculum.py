import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
curriculum = [[] for _ in range(n+1)] # 해당 index를 가진 class를 거쳐야 하는 class번호 저장 

time = [0] * (n+1)
connection = [0] * (n+1)

for i in range(1, n+1) :
    data = list(map(int,input().split()))
    time[i] = data[0]
    for x in data[1:-1] :
        connection[i] += 1 # [0,0,1,1,2,1] , 선행학습할 class 수
        curriculum[x].append(i)
    # [[] , [2,3] , [] , [4,5] , [] , []  ]

result = copy.deepcopy(time)
# a = b 로 리스트를 복사하면 a가 변경될때 b도 영향을 받으므로 deepcopy를 사용해야한다.
q = deque()

for i in range(1,n+1) :
    if connection[i] == 0 :
        q.append(i) 
        # 선행학습이 없는 class일 수록 온전한 수강시간이 나오기때문인가..?

while q :
    now = q.popleft()
    # 리스트에서 list[0] 이렇게 뽑고 삭제하는거랑 결과는 동일하지만 시간이 빠름
    # heap처럼 최소값과는 상관없는 얘기
    for i in curriculum[now] : # now를 선행학습으로 듣고 가야하는 class확인
        result[i] = max(result[i], result[now]+time[i])
        # now를 선행학습으로 듣고가야하는 하므로 now의 학습시간 + 현 class(=i) 학습시간
        connection[i] -= 1 # 현 class(i)를 위해 선행학습한 class를 확인했으니 -1

        if connection[i] == 0 :
            q.append(i)
# 이제 선행학습할 class가없으니 온전한 나의 강의시간이 나왔으므로 이걸 기준으로 또 선행학습 될 class찾기

for i in range(1, n+1) :
    print(result[i])
        

    


'''
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
    '''