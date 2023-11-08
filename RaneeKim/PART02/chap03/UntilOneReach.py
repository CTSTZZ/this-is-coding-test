n,k = map(int, input().split())

result = 0
while n!=1 : # n이 1이 아닐때 while문 진행 -> n==1일때 while문 끝! 
    if n % k != 0 : # n이 k로 나누어 떨어지지 않을 때
        n -= 1
        result += 1
    if n % k == 0 : # 나누어 떨어질때
        n //= k # n값은 k로 나눈 몫 n==16, k==4 이면 n = 4 
        result += 1
print(result)