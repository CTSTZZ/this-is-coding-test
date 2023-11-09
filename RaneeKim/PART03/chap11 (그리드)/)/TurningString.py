import sys
import time
input = sys.stdin.readline

s = input().strip()

start_time = time.time()

list_s = list(map(int,s))

if list_s[0] == 0 :
    count_0 = 1
    count_1 = 0
if list_s[0] == 1 :
    count_0 = 0
    count_1 = 1

for t in range(1,len(list_s)) :
    if list_s[t-1] == list_s[t] :
        continue
    if list_s[t-1] != list_s[t] :
        if list_s[t] == 0 :
            count_0 += 1
        if list_s[t] == 1 :
            count_1 += 1

print(min(count_0,count_1))

end_time = time.time()

print('time : ', end_time-start_time)

