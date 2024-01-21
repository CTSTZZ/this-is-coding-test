import sys
input = sys.stdin.readline

n = int(input().strip())
result = [[0]*(n+1) for _ in range(n+1)]
curriculum = [[0]]
for i in range(n) :
    data = list(map(int,input().split()))
    result[i+1][i+1] = data[0]
    curriculum.append(data[1:-1])

for i in range(len(curriculum)) :
    if i == 0 :
        continue
    if curriculum[i] > 0 :
        
