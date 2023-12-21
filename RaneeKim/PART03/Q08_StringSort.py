import sys
import time

input = sys.stdin.readline

def input_S() : # 입력조건 , 조건안되면 다시 입력하도록
    S = input()
    if 1 <= len(S) <= 10000 : 
        return sorted(list(S)) # list형태,정렬로 리턴 (1,2,3,A,B,C,D,E) 식으로 정렬됨
    else : return(input_S())

def string_sort(S) :
    n = 0
    st = ''
    for ch in s :
        try :
            if int(ch) : # int형이 True라면, 즉 숫자라면
                n += int(ch)
        except Exception as e : # int형으로 변환에서 오류가난다면, 문자라면
            st += ch
    return(print(st,n,sep=""))  # sep안넣어주면 출력 시 문자와 숫자사이 공백이 하나 생김

s = input_S()
start = time.time()
string_sort(s)
end = time.time()
print("time : ", end-start)

'''
>>> s = input_S()
AJKDLSI412K4JSJ9D
>>> string_sort(s)

ADDIJJJKKLSS20
>>> end = time.time()
>>> print("time : ", end-start)
time :  0.018830060958862305
'''