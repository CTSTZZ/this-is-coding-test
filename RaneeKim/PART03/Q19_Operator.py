n = int(input())
data = list(map(int,input().split()))
add, minus, mul, div = map(int,input().split())

minn = 1e9
maxx = -1e9

def solution(i,now) :
    
    global add, minus, mul, div, minn, maxx

    if i == n :
        minn = min(minn,now)
        maxx = max(maxx,now)

    else :
        if add > 0 :
            add -= 1 
            solution(i+1, now + data[i]) 
            add += 1
        if minus > 0 :
            minus -= 1 
            solution(i+1, now - data[i])
            minus += 1
        if mul > 0 :
            mul -= 1 
            solution(i+1, now * data[i])
            mul += 1
        if div > 0 :
            div -= 1 
            solution(i+1, now//data[i])
            div += 1
    
    return maxx,minn


solution(1,data[0])