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