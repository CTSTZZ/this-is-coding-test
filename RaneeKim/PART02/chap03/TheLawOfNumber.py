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