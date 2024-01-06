import sys
input = sys.stdin.readline

def solution() :
    n = input().strip()
    soldier = list(map(int, input().split()))
    count = 0
    for i in range(len(soldier)-1) :
        if soldier[i] <= soldier[i+1] :
            count += 1
    return count

solution()


'''
12 2 5 3 2 10 8 7 15 5 4 3
'''
l = [7,8,9,10,11]


n = input().strip()
soldier = list(map(int, input().split()))
count = 0

def solution() :
    global count
    dele = []
    for i in range(len(soldier)-1) :
        if soldier[i] <= soldier[i+1] :
            dele.append(i+1)
            count += 1
        
    sorted_soldier = sorted(soldier)
    cheak = [i for i in range(len(soldier)) if soldier[i] != sorted_soldier[i]]
    if len(cheak) > 0 :
        return solution()
    else :
        return count

solution()

