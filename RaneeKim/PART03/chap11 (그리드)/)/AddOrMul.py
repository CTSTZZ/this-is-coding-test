import sys
import time
input = sys.stdin.readline

s = input().strip()

start_time = time.time()

list_s = list(map(int,s)) # 문자열을 숫자로 변경
result = list_s[0]

for i in range(1,len(list_s)) :
   
    if list_s[i] <= 1 or result <=1 : 
	    result += list_s[i]
    # if list_s[i] == 0 or result == 0 :
    # 오류발생부분 : or, 1이 중요! result값이나 계산 될 수 둘 중 하나라도 0 or 1 +해야 하기 때문  1일때도 곱하는 것 보다 +가 큰 수가 만들어짐	
    else :
        result *= list_s[i]
        
print(result)

end_time = time.time()
print('time : ' , end_time - start_time)