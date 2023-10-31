# 숫자 입력 받기
n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

# 선택정렬 : 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것

for i in range(len(array)) : # 배열 왼쪽 숫자부터 for문 시작
    min_index = i # 제일 왼쪽에 배열된 숫자가 기준이 됨
    for j in range(i+1,len(array)) : # 왼쪽을 제외한 나머지 숫자들 = 즉, 확인하지 않은 숫자로 for문 시작 
        if array[min_index] > array[j] : # 확인하지 않는 숫자 중 가장 작은 값을 찾는 행위
            min_index = j # 작다면 min_index 값을 바꾼다
    array[min_index] , array[i] = array[i], array[min_index] # 확인하지 않는 숫자 for문이 끝날때 왼쪽에 놓여질 숫자도 바뀜

for i in array :
    print(i, end=' ')

# 삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 

for i in range(len(array)) : # for문을 두개 하는 이유는, 처음은 왼쪽 숫자를 기준으로 - 1번 for문
    for j in range(i+1,0,-1) : # 확인하지 않은 데이터들을 차례로 확인하기 위해 - 2번 for문
        if array[j] < array[j-1] : # 왼쪽으로 가면서 더 작은 숫자라면
            array[j-1] , array[j] = array[j] , array[j-1] #  체인지 
        else :
            break


# 퀵정렬 3 0 6 1 4 2 5
'''
기준데이터 설정 -> 기준데이터(Pivot)보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적으로 첫번째 데이터를 Pivot으로 설정
for i in range(len(array)) : 
    for j in range(i+1,len(array)) :
        if array[j] < array[-j] :
            array[j], array[-j] = array[-j], array[j]
        if j > (i+2)/2 :
            k = int((i+2)/2)
            array[i], array[k] = array[k], array[i]

'''

def quick(data) :

    if len(data) <= 1 : # left와 right로 쪼개서 재귀함수 진행할건데 리스트안에 데이터가 하나밖에 없다면 함수 종료
        return data

    pivot = data[0] # 기준데이터를 정함
    tail = data[1:] # 기준데이터 제외한 리스트
    left = [i for i in tail if i < pivot] # 기준보다 작은 데이터는 왼쪽으로
    right = [i for i in tail if i > pivot] # 기준보다 큰 데이터는 오른쪽으로

    return [quick(left) + pivot + quick(right)] # 왼쪽과 오른쪽 나뉘어서 계속 함수 진행 그리고 왼쪽 + 기준 + 오른쪽 으로 리스트 정렬

