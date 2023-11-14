import sys
import time

input = sys.stdin.readline

def input_S() :
    S = input()
    if 1 <= len(S) <= 10000 :
        return sorted(list(S))
    else : return(input_S())

def string_sort(S) :
    n = 0
    st = ''
    for ch in s :
        try :
            if int(ch) :
                n += int(ch)
        except Exception as e :
            st += ch
    return(print(st,str(n)))

s = input_S()
start = time.time()
string_sort(s)
end = time.time()
print("time : ", end-start)

'''
>>> s = input_S()
AJKDLSI412K4JSJ9D
>>> string_sort(s)

ADDIJJJKKLSS 20
>>> end = time.time()
>>> print("time : ", end-start)
time :  20.305060386657715
>>>
'''