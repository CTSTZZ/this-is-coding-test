import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip()) # 탑승구수
plane = int(input().strip()) # 비행기수

docking = [1] + ([0]*(n+1)) # 도킹된 비행기 체크용


for i in range(plane+1) : 
    q = deque() # 그냥 list보다 시간이 더 빠르므로
    exitt = int(input().strip()) # 도킹할수있는 출입구
    for e in range(exitt+1) : #
        q.append(e) # 도킹할수 있는 출입구 넘버를 appending [0,1,2,3,4]
    cheak = 0 # 도킹을 얼마나 시도 했는지 체크용
    while q :
        a = q.pop() # 제일 큰 출입구 넘버를 빼낸다
        if docking[a] == 0 : # 그 출입구에 도킹한 비행기가 없으면
            docking[a] = 1 # 1로 바꿔서 도킹 되었다고 표시해둠
            #  [1, 0, 0, 0, 0, 0]  --> [1, 1, 1, 1, 0, 0]
            break
        cheak += 1 # 도킹시도 한번했으닌깐 +1
        
    if cheak == len(range(e+1)) : 
        result = i
        break

print(result)