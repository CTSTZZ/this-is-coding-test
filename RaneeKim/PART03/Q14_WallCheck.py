from itertools import permutations


# n:외벽길이 , weak:취약부분 , dist:친구들이갈수있는거리
def solution(n,weak,dist) : 
    length = len(weak) # 취약부분 개수
    print(length)
    for i in range(length) :
        weak.append(weak[i]+n) # 원형을 일자로 푸는 과정(외벽길이만큼더함,시계라고생각) 1,3,4,9,10 -> 1,3,4,9,10, 13,15,16,21,22 
    answer = len(dist) + 1
    print(length)
    # 최소값을 찾는 것 -> min(A,B)를 사용해서 찾는것이므로 초기값의 answer은 실제 답이될수 있는 최대값(친구들수)보다 무조건 커야함
    # 최소값 찾는 다른 문제에서 1e9로 초기화 시켰던것과 같은 원리

    for start in range(length) : # (0 ~ 취약부분spot개수-1) 을 각각 시작점으로 설정 
        for friends in list(permutations(dist, len(dist))) : # 순열을 통해 친구(거리)를 나열할 수 있는 모든 조합을 생성
            # [ [3,5,7] , [3,7,5] , [5,3,7] , [5,7,3] , [7,3,5] , [7,5,3] ]
            
            count = 1 # 투입할 친구의 수
            position = weak[start] + friends[count-1]
            # position = 취약부분spot + 투입된친구수-1 의 index에 해당하는 친구가갈수있는거리 -> 해당 친구가 확인할 수 있는 마지막 위치
                                        #-> 즉 정렬된 거리 list의 첫번째 거리부터 확인 , count는 1로 초기화되어있으므로 -1을 해야함

            for index in range(start,start+length) : # 시작점 ~ 취약점의 모든 부분 확인
                if position < weak[index] : # 확인을 하다가 위에서 정한 친구가 확인할 수 있는 마지막 위치보다 오버된 취약 spot이 있으면 
                    count += 1 # 친구한명 더 추가
                    if count > len(dist) : 
                        break # 친구 투입이 불가하면 종료
                    position = weak[index] + friends[count-1] # 그 다음 친구가 확인할 수 있는 마지막 위치 설정
            answer = min(answer,count) # min(초기화된 answer(친구+1) , for문 종료 후 투입된 친구수)
    if answer > len(dist) : # 최종답이 친구수보다 많다면 -1 반환
        return -1
    return answer 
