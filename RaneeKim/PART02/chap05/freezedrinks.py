def conection(x,y) :

    if x<=-1 or y<=-1 or x>=n or y>=m :
        return False

    if drinks[x][y] == 0 :
        drinks[x][y] = 1
        
        conection(x-1,y)
        conection(x,y-1)
        conection(x+1,y)
        conection(x,y+1)
        return True
    
    return False
    

n,m = map(int, input().split())

drinks = []
for i in range(n) :
    data = list(map(int, input()))
    drinks.append(data)

result = 0

for i in range(n) :
    for e in range(m) :
        if conection(i,e) == True :
            result +=1

print(result)