# 수빈씌 방법
# min을 사용하는 방법 생각해보기 ~!
import math
count = 0

def sosu(x) :
    for i in range(2, int(math.sqrt(x)) + 1) :  # range(2, x+1) 도 가능
        if x % i == 0 :
            return False
        return x

def cal(x):
    # 전역변수로 count 사용
    global count
    # 입력받은 숫자 한자리씩 쪼개기
    num_list = list(map(int, str(x)))

    # x가 1이라면 count 출력
    if x == 1:
        return count
    # x의 1의자리가 1이거나 6이면 1빼주기
    elif sosu(x) :
        x -= 1
        count += 1
        return cal(x)
    elif x%5 == 0:
        x = int(x/5)
        count += 1
        return cal(x)
    elif x%3 == 0:
        x = int(x/3)
        count += 1
        return cal(x)
    elif x%2 == 0:
        x = int(x/2)
        count += 1
        return cal(x)
    

    def cal(x):
    # 전역변수로 count 사용
    global count
    # 입력받은 숫자 한자리씩 쪼개기
    num_list = list(map(int, str(x)))

    # x가 1이라면 count 출력
    if x == 1:
        return count
    # x의 1의자리가 1이거나 6이면 1빼주기
    elif num_list[-1] == 1 or num_list[-1] == 6:
        x -= 1
        count += 1
        return cal(x)
    elif x%5 == 0:
        x = int(x/5)
        count += 1
        return cal(x)
    elif x%3 == 0:
        x = int(x/3)
        count += 1
        return cal(x)
    elif x%2 == 0:
        x = int(x/2)
        count += 1
        return cal(x)