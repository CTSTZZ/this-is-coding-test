n = int(input())
data = list(map(int,input().split())) # 1,2,3,4,5,6
add, minus, mul, div = map(int,input().split())

# 비교를 위해 
minn = 1e9
maxx = -1e9

def solution(i,now) :
    
    global add, minus, mul, div, minn, maxx

    if i == n : # 한 연산을 거칠때마다 i+1이라는 작업을 하므로 i = n이 되었을때 최소값과 최대값을 반환
        minn = min(minn,now)
        maxx = max(maxx,now)

    else :
        if add > 0 : # add 2 , minus 1, mul 1, div 1 
            add -= 1  # 한 번 add연산을 했으므로 -1
            solution(i+1, now + data[i])  # add연산은 -1 한 상태로 재귀함수로 두번째 solution함수를 호출
        # 함수호출 -> add=2 에서 1 -> 재귀함수호출 add=1 에서 0 -> 재귀함수호출 minus=1 에서 0 -> 재귀함수호출 mul=1 에서 0 ->...           
            add += 1 
            # 한 번 add연산한 상태는 재귀함수로 호출했으니, add 연산 count를 다시 초기화 하는 단계
            # - + + * /
        if minus > 0 :
            minus -= 1 
            solution(i+1, now - data[i])
        # 함수호출 -> minus=1 에서 0 -> 재귀함수호출 add=2 에서 1 -> 재귀함수호출 add=1 에서 0 -> 재귀함수호출 mul=1 에서 0 ->... 
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