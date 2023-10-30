

'''
n,m = map(int, input().split())
x,y,d = map(int, input().split())

map_array = []
for i in range(n) :
    map_list = []
    for q in range(m) :
        k = int(input())
        map_list.append(k)
    map_array.append(map_list)

dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1] # turn_left 함수 사용하지않기위해 동남서북으로 코딩했으나 실패

def turn_left() :
    global d
    d -= 1
    if d == -1 :
        d = 3

count = 1
turn_count = 0

while True :

    map_array[x][y] = 1
    turn_left()
    nx = x + dx[d] # nx나 ny가 <0 or >m,n 어떻게 해야하는지? 즉 n*m을 벗어날때
    ny = y + dy[d]
    
    if nx<0 :
        nx = 0
    if ny<0 :
        ny = 0
    if nx>=n :
        nx = n-1
    if ny>=m :
        ny = m-1

    if map_array[nx][ny] == 0 :
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue

    if map_array[nx][ny] == 1 :
        turn_count += 1

    if turn_count == 4 :
        turn_count = 0
        x = x - dx[d]
        y = y - dy[d]
        if map_array[x][y] == 0 :
            count += 1
        if map_array[x][y] == 1:
            break

print(count)
'''