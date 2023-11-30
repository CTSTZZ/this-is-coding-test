import sys
input = sys.stdin.readline

def finding() : 
    n= int(input().strip())
    num_list = sorted(list(map(int, input().split())))
    fixed = -1
    
    for i in range(len(num_list)) :
        if i == num_list[i] :
            fixed = i

    return fixed


finding()