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
    student = dict(sorted(dict(student).items(), key=lambda x:x[1]))
    result = list(student.keys())

    for i in result :
        print(i, end = ' ')


n, student = input_n()
printout(student)


'''
>>> n, student = input_n()
3
이순신 77
유관순 63
홍길동 95
>>> printout(student)
유관순 이순신 홍길동 >>> 
'''