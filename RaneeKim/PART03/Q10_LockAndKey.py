def match(arr, key, rot, r, c) :
    n = len(key)
    for i in range(n) :
        for j in range(n) :
            if rot == 0 :
                arr[r+i][c+j] += key[i][j] # 
            elif rot == 1 : # [3,0]이 [0,0] , [3,3]이 [0,3] 으로 돌려짐
                arr[r+i][c+j] += key[n-1-j][i]
            elif rot == 2 : 
                arr[r+i][c+j] += key[n-1-i][n-1-j]
            else :
                arr[r+i][c+j] += key[j][n-1-i]

def check(arr, offset,n) :
    for i in range(n) :
        for j in range(n) :
            if arr[offset+i][offset+j] != 1 : # 모든 자물쇠구멍을 확인했을 때 1이 아니면
                return False # False 반환
    return True # False 반환안되었다면 = 모든 자물쇠구멍이 1이라면 = True반환


def solution(key,lock) :
    offset = len(key) - 1

    for r in range(offset+ len(lock)) : # 행으로 얼마나 움직이는지
        for c in range(offset + len(lock)) : # 열로 얼마나 움직이는지
            for rot in range(4) : # 90도로 4번 돌려서 다 확인해야함
                arr = [[0 for _ in range(58)] for _ in range(58)] 
                # 58인 이유는 키랑 자물쇠가 최대 20이므로 나올수 있는 최대 배열은 겹쳐지는 곳 한군데씩 총 2개를 뺀 58
                # 자물쇠 복사하는 단계
                for i in range(len(lock)) :
                    for j in range(len(lock)) : 
                        arr[offset+i][offset+j] = lock[i][j] # offset만큼 떨어진곳에 자물쇠를 놔두기로했으니

                match(arr, key, rot, r, c) 
                # 배열(중간에 자물쇠와 열쇠가 돌아가게만드는 배열), 열쇠값, 90도로 얼마나 돌아갔나, 행, 열

                if check(arr,offset, len(lock)) :
                    return True
    return False


'''
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

'''