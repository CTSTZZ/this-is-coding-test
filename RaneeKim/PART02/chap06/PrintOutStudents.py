import sys
input = sys.stdin.readline

def input_n() :
    n = int(input().strip())
    student = []
    for _ in range(n) :
        s = list((input().split()))
        student.append(s)
    
    return n, student

def printout (student) :
    student = dict(student)
    student = dict(sorted(student.items(), key=lambda x:x[1]))
    result = list(student.keys())

    return print(result)


n, student = input_n()
printout(student)

'''
>>> n, student = input_n()
3
홍길동 70
이순신 64
유관순 85
>>> printout(student)
['이순신', '홍길동', '유관순']

'''