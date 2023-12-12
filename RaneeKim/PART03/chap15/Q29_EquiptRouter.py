def solution() :
    n,c = map(int,input().split()) 
    router = []
    for _ in range(n) : # 1 2 4 8 9 13 15 일때는 어쩌지..
        router.append(int(input().strip()))
    router.sort()
    
    min_gap = 1
    max_gap = router[-1] - router[0]   

    while min_gap < max_gap :
        mid_gap = (max_gap + min_gap) // 2  
        e = router[0]
        count = 1
        for i in router :
            if i >= e + mid_gap :
                count += 1
                e = i
        if count < c : # 공유기가 c보다 더 작게 설치됨 -> gap이 너무 큼 -> gap을 감소
            max_gap = mid_gap-1 # 7
        else : # 공유기가 c보다 같거나 크게 설치됨 -> 일단 1차조건만족(result값으로 기록) -> 그러나 gap의 최댓값을 찾아야 하므로 gap을 증가
            min_gap = mid_gap + 1 
            result = mid_gap
    
    return print(result)
        

