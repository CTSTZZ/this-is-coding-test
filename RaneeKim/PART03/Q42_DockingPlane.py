import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip()) # 탑승구수
plane = int(input().strip()) # 비행기수

docking = [1] + ([0]*(n+1)) # 도킹된 비행기 체크용


for i in range(plane+1) : 
    q = deque() # 그냥 list보다 시간이 더 빠르므로
    exitt = int(input().strip()) # 도킹할수있는 출입구
    for e in range(exitt+1) :
        q.append(e) # 도킹할수 있는 출입구 넘버를 appending [0,1,2]
    cheak = 0 # 도킹을 얼마나 시도 했는지 체크용
    while q :
        a = q.pop() # 제일 큰 출입구 넘버를 빼낸다
        if docking[a] == 0 : # 그 출입구에 도킹한 비행기가 없으면
            docking[a] = 1 # 1로 바꿔서 도킹 되었다고 표시해둠
            #  [1, 0, 0, 0, 0, 0]  --> [1, 0, 1, 0, 0, 0]
            break
        cheak += 1 # 도킹시도 한번했으닌깐 +1
        
    if cheak == len(range(e+1)) : 
        result = i
        break

print(result)

''' 
도킹시도 카운트수가 출입구넘버 최대수 + 1 이면 
result값을 현재 도킹시도했던 비행기 넘버 수로 정하고 break
왜 출입구넘버(2,2,3,3,4,4)의 +1이냐?
0 1 2 -> 도킹시도카운드 1
0 1 2 -> 도킹시도카운드 2
0 1 2 3 -> 도킹시도카운드 1
0 1 2 3 -> 도킹시도카운드 4 
(이미 3,2,1 출입구 순으로 했을때 실패인걸 알았지만 0까지 시도 해봐야 진짜 실패인걸 안다)

0 1 2 3 4  -> 도킹시도카운드 1
0 1 3 -> 도킹시도카운드 1
0 1 2 3 -> 도킹시도카운드 2
0 1 2 3 4  -> 도킹시도카운드 4 
만약 출입구넘버수+1 이 아니라 출입구넘버였으면 이 예시도 실패로 간주하고 result값으로 3을 반환할것이기때문

왜 i+1이 아니라 i인가?
도킹이 성공한 비행기 수를 반환하는데
3번까지 성공하고 (for은 0,1,2까지 돌아감, 이때는 i=2)
4번 비행기를 시도해보니 실패 (for은 0,1,2,3까지 돌아감, 이때는 i=3)
정답은 3을 반환해므로 굳이 i+1이 아닌 i를 반환

'''    