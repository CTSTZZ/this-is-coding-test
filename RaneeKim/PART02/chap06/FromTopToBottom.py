# 숫자 입력 받기
n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

# 선택정렬 27 23 39 30 3 5 7
'''

'''
for i in range(len(array)) :
    min_index = i
    for j in range(i+1,len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[min_index] , array[i] = array[i], array[min_index]

for i in array :
    print(i, end=' ')

'''
for i in range(array) :
    for j in range(array)
    if array[j+1] <= array[j+2] :
'''


# 삽입정렬

# 퀵정렬