n,m,k = map(int, input().split())
data = []
for i in range(0,n) :
    a = int(input())
    data.append(a)

data.sort(reverse=True)
count = 0
sub_count = 0
result = 0

while count < m :
    while sub_count != k :
        if count >= m :
            break
        result += data[0]
        sub_count += 1
        count += 1

    while sub_count == k :
        if count >= m :
            break
        result += data[1]
        sub_count = 0
        count += 1

print(result)

# break가 핵심인것같음

'''
# 1
n,m,k = map(int, input().split())
data = []
for i in range(0,n) :
    a = int(input())
    data.append(a)
count = 0

for i in range(0,m) :
    if count < k :
        result += data[0]
        count += 1
    if count > k :
        result += data[1]
        count = 0

print(result)
# count = k 일때 result 더하는 if문이 둘다 실현되어서 틀린 코드

# 2
n,m,k = map(int, input().split())
data = []
for i in range(0,n) :
    a = int(input())
    data.append(a)

data.sort(reverse=True)
count = 0
sub_count = 0
result = 0


while count < m :
    while sub_count != k : # count < m이 되어도 i = k일때 while문이 돌아가므로 result값이 늘어남
        result += data[0]
        sub_count += 1
        count += 1
    result += data[1]
    sub_count = 0
    count += 1

print(result)


????? 정답에서 data(list)입력할 때 n을 사용해야하는거 아닌가?
'''