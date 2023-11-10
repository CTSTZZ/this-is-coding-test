import sys
import time
input = sys.stdin.readline # 마지막 /n까지 같이 출력이 되어서

n = int(input().strip()) # strip()을 꼭 넣어줘야함
coin = list(map(int, input().split()))

start = time.time

coin.sort()
cannot = 1
for c in coin :
    if cannot < c :
        break
    cannot += c

print(cannot)

'''
cannot = 0

while True :
    cannot += 1 # 1부터 최소값이 나올때까지 하나하나 확인해보자 생각했는데 개쓰레기 생각~~ㅠ
    result = cannot  
    for c in coin :
        result -= c
        if result == 0 :
            break
        if result < 0 : # 무한루프 걸려서 끝나지 않음
            print(cannot)
            break
'''
        

