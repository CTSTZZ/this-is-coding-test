def match(arr, key, rot, r, c) :
    n = len(key)
    for i in range(n) : # 열쇠를 복사하기 위해 열쇠 크기만큼
        for j in range(n) :
            if rot == 0 :
                arr[r + i][c + j] += key[i][j] # 더했을때 2가되면 안 맞으닌깐 
            elif rot == 1 :
                arr[r + i][c + j] += key[n-1-j][i] # 90도로 돌렸으닌깐 자리가 바꼈는걸 표현함
            elif rot == 2 :
                arr[r + i][c + j] += key[n-1-i][n-1-j]
            else :
                arr[r + i][c + j] += key[j][n-1-i]

def check(arr, offset, n) :
    for i in range(n) :
        for j in range(n) :
            if arr[offset + i][offset + j] != 1
                return False
    return True

def solution(key, lock) :
    offset = len(key) -1 # 키와 자물쇠가 떨어진 길이, 적어도 하나는 겹치기 때문
     
    for r in range(offset+len(lock)) : # 가로움직임
        for c in range(offset + len(lock)) : # 세로움직임
            for rot in range(4) : # 시계 방향으로 90도 돌리는 것
                arr = [[0 for _in range(58)] for _ in range(58)]  # 자물쇠 길이 최대 20이고 2개는 겹치므로
                for i in range(len(lock)) : # 자물쇠 복사
                    for j in range(len(lock)) : 
                        arr[offset + i][offset + j] = lock[i][j]
                
                match(arr,key,rot,r,c) # 복사하기 위한 함수
                if check(arr, offset, len(lock)) : # 값이 모두 1인걸 확인하는 함수
                    return True

    return False 