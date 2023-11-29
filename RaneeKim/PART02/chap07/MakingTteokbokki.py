import sys
input = sys.stdin.readline

def solution() :
    n,m = map(int,input().split())
    tteok = sorted(list(map(int, input().split())))

    start = 0
    end = max(tteok)
    summ = 0

    while sum != m :
        summ = 0
        midd = (end+start)//2
        for i in tteok : 
            if i <= midd :
                summ += 0
            else :
                summ += (i-midd)
        if summ > 6 :
            start = midd + 1
        if summ < 6 :
            end = midd - 1
    
    return midd


solution()
    