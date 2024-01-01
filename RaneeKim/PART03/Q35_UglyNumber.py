import sys
input = sys.stdin.readline

def solution() :
    n = input().strip()
    ugly = [1]
    i = 0
    while len(ugly) <= n :
        i += 1
        i2 = i3 = i5 = 0
        i2 = i * 2
        ugly.append(i2)
        i3 = i * 3
        ugly.append(i3)
        i5 = i * 5
        ugly.append(i5)
        ugly = sorted(list(set(ugly)))

    return(print(ugly[n-1]))

'''
1 * 2 = 2
1 * 3 = 3
1 * 5 = 5
1,2,3,5

2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
1,2,3,4,6,8
'''