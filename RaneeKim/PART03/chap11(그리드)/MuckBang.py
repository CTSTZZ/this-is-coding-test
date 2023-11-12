def solution (food_times,k) :
    global result_food, result_num
    for t in range(len(food_times)) : # food_times 리스트를 for문으로 돌리기
        if food_times[t] > 0 :
            food_times[t] = food_times[t] - 1 # time이 0보다 크면 -1하고 그 값을 리스트에 저장
            k -= 1 # k는 음식 한번 먹을때마다 -1이므로
        else : continue
        if k == 0 : # 이렇게 돌다가 만약 k=0 이면 새로운리스트 (result_food)에 지금 멈춘상태의 food_times리스트를 저장함
            result_food = food_times
            result_num = t+1 # 먹방이 끝난 다음 음식부터 시작이므로 +1
    if k <= 0 :
        return result_food, result_num # food_times 리스트 for문이 끝나면  result_food와 result_num을 반환하고 함수 끝
        
    if food_times == [0] * len(food_times) : # food_times에 있는 모든 값이 0일때를 명시해주지 않으면 무한루프가 됨으로 if문으로 명시함
        return food_times, t # k,t 아무숫자나 상관없음 어차피 음식시간은 다 0이므로 어디부터 시작하든 노상관~
        
    return solution(food_times,k) 
    # 함수에서는 for문이 한번 돌아감 따라서 먹방시간인 k가 다 지나지 않고 food_times의 for문이 끝날수도 있으니 그때는 재귀함수로 다시 호출

food_time = list(map(int,input().split()))
turning = int(input())
turn_food,numm = solution(food_time,turning) # 함수로 반환된 값(result_food,result_num)

for _ in range(len(turn_food)) :
    if numm < len(turn_food) :
        numm = numm
    else :  # nummm값이 리스트길이를 넘으면 다시 리스트의 처음으로 돌아가서 리스트의 모든 숫자를 확인해야 하므로
        numm -= len(turn_food) 
    if turn_food == [0] * len(turn_food) : # 리스트의 모든값이 0 (=먹을 음식이 없으면) -1을 반환
        print(-1)
        break
    if turn_food[numm] == 0 : # 확인한 음식 시간이 0이면 다음 음식 확인
        numm += 1
    elif turn_food[numm] > 0 : # 확인 중 시간이 남은 음식이 있으면
        print(numm+1) # 그 음식의 번호를 출력해줌 +1인 이유는 리스트 배열 상 numm+1번째 번호의 index값은 numm 이므로
        break

