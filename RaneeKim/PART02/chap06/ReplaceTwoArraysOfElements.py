import sys
input = sys.stdin.readline

def input_N() :
    n,k = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    return n,k,list_a,list_b

def replace(k,list_a,list_b) :
    for _ in range(k) :
        list_a = sorted(list_a)
        list_b = sorted(list_b)
        a = min(list_a)
        b = max(list_b)
        if a < b :
            list_a[0] = b
            list_b[-1] = a
    
    return print(sum(list_a))


n,k,list_a,list_b = input_N()
replace(k,list_a,list_b) 

'''
>>> n,k,list_a,list_b = input_N()
5 3
1 2 5 4 3
5 5 6 6 5
>>> replace(k,list_a,list_b) 
26
>>>
'''