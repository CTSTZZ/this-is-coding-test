import sys
input = sys.stdin.readline

def solution() :
    n = input().strip()
    k = len(n) // 2

    left = 0
    right = 0
    
    for i in range(len(n)) :
        if i < k :
            left += int(n[i])
        else :
            right += int(n[i])
    
    if left == right :
        return print("LUCKY")
    else :
        return print("READY")

solution()


'''
import sys
import time

input = sys.stdin.readline

def input_N() :
    N = input().strip() 
    if 10 <= int(N) <= 99999999 and len(N)%2 == 0 : 
        return int(N) # 정수로 받으라고 적혀져있어서
    return (input_N())

def Lucky(S) :
    list_n = [int(n) for n in str(S)] # 각 자리수를 리스트 하나씩 넣도록 하려고
    count_l = count_r = 0
    for i in range(len(list_n)//2) :
        count_l += list_n[i]
    for i in range(len(list_n)//2,len(list_n)) :
        count_r += list_n[i]
    if count_l == count_r :
        return print("LUCKY") 
    else : 
        return print("READY")

n = input_N()
start = time.time()
Lucky(n)
end = time.time()
print("time : ", end-start)

>>> n = input_N()
12345
1234567898
123402
>>> start = time.time()
>>> Lucky(n)
LUCKY
>>> end = time.time()
>>> print("time : ", end-start)
time :  0.0009856224060058594
'''

'''
def input_N() :
    N = input().strip() # N은 str형
    if 10 <= int(N) <= 99999999 and len(N)%2 == 0 :  # 입력조건 안써줘도 맞긴맞음(백준확인완)
        return int(N) # 정수를 반환한다고 했으니 int형으로
    return (input_N())

def Lucky(S) :
    list_n = [int(n) for n in str(S)] # 자리수에 맞춰 하나씩 꺼내주기 위하여
    count_l = count_r = 0
    for i in range(len(list_n)//2) : # 왼쪽 반
        count_l += list_n[i]
    for i in range(len(list_n)//2,len(list_n)) : # 오른쪽 반
        count_r += list_n[i]
    if count_l == count_r : # 같으면 럭키
        return print("LUCKY") # 백준에서 에러 났던 부분 : print를 안쓰고 return "LCUKY만 해줘서"
    else : 
        return print("READY") # 다르면 레뒤
'''