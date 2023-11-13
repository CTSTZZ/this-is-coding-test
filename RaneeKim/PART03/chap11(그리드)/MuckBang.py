import sys
import time
input = sys.stdin.readline

food_time = list(map(int,input().split()))
turning = int(input().strip())

start = time.time()

def solution (food_times,k) :
    if sum(food_times) <= k :
        return -1 

    for t in range(len(food_times)) : 
        if food_times[t] > 0 :
            food_times[t] = food_times[t] - 1  
            k -= 1   
        else : continue
        if k == 0 :  
            t += 1 
            for _ in range(len(food_times)) :
                if t >= len(food_times): 
                    t -= len(food_times)
                if food_times[t] == 0 : 
                    t += 1
                elif food_times[t] > 0 : 
                    return (t+1) 
    
    if k > 0 :
        return solution(food_times,k)

solution (food_time,turning)
end = time.time()
print('time : ',end-start)


'''
>>> food_time = list(map(int,input().split()))
3 2 1 3 2 7
>>> turning = int(input().strip())
15
>>> solution (food_time,turning)
6
>>> end = time.time()
>>> print('time : ',end-start)
time :  0.19494891166687012
'''

''' 최종코드 : 프로그래머스 기준 정확도 통과, 효율성X

def solution (food_times,k) :
    if sum(food_times) <= k : # 전체 음식시간이 방송시간보다 적으면 무조건 -1 반환
        return -1 

    for t in range(len(food_times)) :  # food_times 리스트를 for문으로 돌리기
        if food_times[t] > 0 :
            food_times[t] = food_times[t] - 1  # time이 0보다 크면 -1하고 그 값을 리스트에 저장
            k -= 1   # k는 음식 한번 먹을때마다 -1이므로
        else : continue
        if k == 0 :  # 이렇게 돌다가 만약 k=0 이면 
            t += 1 # t 즉, food_times 리스트에서 음식 확인할 index를 +1 해줌 (다음 음식을 확인하기 때문)
            for _ in range(len(food_times)) : # food_times 안에 음식 시간을 for문으로 모두확인
                if t >= len(food_times): 
                    t -= len(food_times)
# t가 food_times길이를 넘으면 다시 첫번째 순서로
                if food_times[t] == 0 :  # 단, 방송이 다시 시작되는 t번째부터 확인함
                    t += 1
                elif food_times[t] > 0 : # 시간이 남은 음식이 나오면
                    return (t+1) # 음식번호 반환. 단, list배열구조 상 음식 번호는 index+1 이므로 +1을 함

            # 새로운 변수에 저장하는 이유는 for문이 끝나지 않았으므로 k가 계속돌아가고 food_times의 숫자들이 계속 바뀌기 때문

    if k > 0 :
        return solution(food_times,k)
    # 함수에서는 for문이 한번 돌아감 따라서 먹방시간인 k가 다 지나지 않고 food_times의 for문이 끝날수도 있으니 그때는 재귀함수로 다시 호출

solution (food_time,turning)

'''

''' 첫번째 코드 : vs에서는 돌아가고 정답도 나오는데 프로그래머스에서 자꾸 틀렸다고함 ㅡㅡ 
                return값으로 정답을 반환해야하는데 print로 해서 그런거 아닐까 의심중

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

'''

''' 두번째 코드 : 프로그래머스 기준 26/32 통과, 효율성은 통과X

def solution (food_times,k) :
    if sum(food_times) <= k :
        return -1 
    
    global result_food, result_num
    for t in range(len(food_times)) : 
        if food_times[t] > 0 :
            food_times[t] = food_times[t] - 1 
            k -= 1 
        else : continue
        if k == 0 :
            result_food = food_times
            result_num = t+1 
    if k > 0 :
        return solution(food_times,k)
    if k <= 0 :
        food_times = result_food
        numm = result_num

    for _ in range(len(food_times)) :
        if numm < len(food_times) :
            numm = numm
        else : 
            numm -= len(food_times) 
        if food_times[numm] == 0 : 
            numm += 1
        elif food_times[numm] > 0 : 
            return (numm+1)
'''