n,m = map(int, input().split())
find_max = []

for _ in range(n) :
    a = list(map(int, input().split()))
    min_value = min(a)
    find_max.append(min_value)

#  'list' object is not callable 오류가 뜸 -> 리스트 이름이 함수 이름일 때 나타나네요

print(max(find_max))