def solution (food_list,turning) :
    global result_food, result_num
    for t in range(len(food_list)) :
        if food_list[t] > 0 :
            food_list[t] = food_list[t] - 1
            turning -= 1
        else : continue
        if turning == 0 :
            result_food = food_list
            result_num = t+1
    if turning <= 0 :
        return result_food, result_num
        
    if food_list == [0] * len(food_list) :
        return food_list, t
        
    return solution(food_list,k)

food_times = list(map(int,input().split()))
turning = int(input())
turn_food,numm = solution(food_times,turning)

for _ in range(len(turn_food)) :
    if numm < len(turn_food) :
        numm = numm
    else :
        numm -= len(turn_food)
    if turn_food == [0] * len(turn_food) :
        print(-1)
        break
    if turn_food[numm] == 0 :
        numm += 1
    elif turn_food[numm] > 0 :
        print(numm+1)
        break

