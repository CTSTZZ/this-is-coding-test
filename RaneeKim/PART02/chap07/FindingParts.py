# 매장 소유 부품 입력받기
n = int(input()) 

shop_parts = [] 
for _ in range(n) :
    shop_parts.append(int(input()))


# 손님 문의 부품 입력받기
m = int(input()) 
parts = []
for _ in range(m) :
    parts.append(int(input()))


# 결과값을 기본으로 no로 셋팅
result = ['no']*m


for i in range(len(shop_parts)) : # 손님 문의 부품과
    for j in range(len(parts)) : # 매장 소유 부품
        if shop_parts[i] == parts[j] : # 비교후 있으면
            result[j] = 'yes' # 결과값을 yes로 변경


for r in result : # 문제에서 원하는 출력값을 내주기 위한 코드
    print(r, end = ' ')