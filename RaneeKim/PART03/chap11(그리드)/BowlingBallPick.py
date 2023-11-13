import sys
import time

input = sys.stdin.readline

def input_weigt() :
    N,M = map(int, input().split())
    K = list(map(int, input().split()))
    return N,M,K

n,m,k = input_weigt()

for i in k : # 조건을 만족하지 않으면 다시 input받는 코드
    while n < 1 or n > 1000 or m < 1 or m > 10 or i < 1 or i > m  :
        n,m,k = input_weigt() # 무한루프걸리긴함 왜일까,,,,,, # 럭키스트레이트에서 해결완

start = time.time()

weigts = []

for w1 in k :
    for w2 in k :
        if w1 != w2 :
            b = [w1,w2]
            weigts.append(b)

print(len(weigts)//2) # /2 하는 이유는 for문을 돌릴때 처음(처음~끝)~끝 이런식으로 중복으로 돌아갔으므로 /2
end = time.time()
print('time : ', end-start)

'''
7 5
1 2 3 2 4 5 3

19
time :  0.06239628791809082

'''