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


def answer(array, start, end) :
    if start > end :
        return None # 재귀함수 끝나고도 고정점이 없으면 -1 반환
    mid = (start+end) // 2
    
    if array[mid] == mid :
        return mid
    elif array[mid] > mid : # 고정점이 array[mid]를 기준으로 왼쪽에 있음, 오름차순 정렬이기에 가능 ex) -15 1 4 7 9 -> 왼쪽편만본다
        return answer(array, start, mid-1)
    else : # 고정점이 array[mid]를 기준으로 오른쪽에 있음 ex) -15 -14 1 3 7 -> 왼편만 본다
        return answer(array, mid+1, end)


n= int(input().strip())
num_list = sorted(list(map(int, input().split())))
n, num_list
answer(num_list, 0, n-1)
