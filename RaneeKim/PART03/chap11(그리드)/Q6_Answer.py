import heapq

def solution(food_times, k):
    if sum(food_times) <= k :
        return -1
    
    q = []
    for i in range(len(food_times)) : # (음식시간,음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0 
    previous = 0
    length = len(food_times)
    
    # (sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수) 와 k 비교
    while sum_value + ((q[0][0]-previous)*length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에 몇 번ㅉ 음식인지 확인하며 출력
    result = sorted(q,key = lambda x:x[1]) # 음식의번호 기준으로 정렬

    return result[(k - sum_value) % length][1]