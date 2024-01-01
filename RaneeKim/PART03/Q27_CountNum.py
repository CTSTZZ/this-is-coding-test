import sys
input = sys.stdin.readline

def count_num() :
    n,k = map(int, input().split())
    num_list = sorted(list(map(int, input().split())))

    count = num_list.count(k)
    if count == 0 :
        count = -1
    
    return count

count_num()