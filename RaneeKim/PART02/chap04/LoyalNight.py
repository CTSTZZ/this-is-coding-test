n,m = (input())
horizontality = ['a','b','c','d','e','f','g','h']
for i in range(0,8):
    if n == horizontality[i] :
        n = int(i)
m = int(m)
m = m-1   

moving = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
count = 0

for move in moving :
    result = [n + move[0], m+move[1]]
    if result[0] < 8 and result[1] < 8 and result[0] >= 0 and result[1] >= 0 :
        count += 1

print(count)