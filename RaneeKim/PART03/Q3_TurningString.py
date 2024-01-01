import sys
import time
input = sys.stdin.readline

s = input().strip()

start_time = time.time()

list_s = list(map(int,s))

if list_s[0] == 0 : # 첫번째 숫자에 따라서 count_0 or 1 을 카운팅
    count_0 = 1
    count_1 = 0
if list_s[0] == 1 :
    count_0 = 0
    count_1 = 1

for t in range(1,len(list_s)) :
    if list_s[t-1] == list_s[t] : # 이전 숫자와 같으면 밑에 무시하고 다음 반복으로 넘어감 (continue의 역할)
        continue
    if list_s[t-1] != list_s[t] : # 이전숫자와 다르면 counting 시작
        if list_s[t] == 0 :
            count_0 += 1
        if list_s[t] == 1 :
            count_1 += 1

print(min(count_0,count_1)) # 0 과 1 카운팅갯수중 작은거 반환

end_time = time.time()

print('time : ', end_time-start_time)

