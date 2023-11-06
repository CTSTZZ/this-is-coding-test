n,m = map(int, input().split())
find_max = []

for _ in range(n) :
    a = list(map(int, input().split()))
    min_value = min(a)
    find_max.append(min_value)

print(max(find_max))