def conection(x,y) :

    if x<=-1 or y<=-1 or x>=n or y>=m :
        return False  # 범위 벗어나면 즉시 종료
    
    if drinks[x][y] == 0 : # 연결되어있는 부분
        drinks[x][y] = 1 # 연결되어있지않은 부분
        
        # 재귀함수
        conection(x-1,y) # 좌측
        conection(x,y-1) # 상측
        conection(x+1,y) # 우측
        conection(x,y+1) # 하측
        return True # 상하좌우 연결된 곳을 다 돌았으면 True값 반환
    
    return False 
    
n,m = map(int, input().split())

drinks = []
for i in range(n) :
    data = list(map(int, input()))
    drinks.append(data)

result = 0

for i in range(n) :
    for e in range(m) : # 이게 왜 DFS인지는 아직 모르겠넹ㅠ
        if conection(i,e) == True : # 상하좌우 막히지 않은곳 다 도는 행위
            result +=1

print(result)