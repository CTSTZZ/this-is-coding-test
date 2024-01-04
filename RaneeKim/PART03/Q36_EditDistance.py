'''
sunday
saturday
'''
str1 = 'sunday'
str2 = 'saturday'



def solution(str1,str2) :
    str1 = [i for i in str1]
    str2 = [i for i in str2]

    n = len(str1)
    m = len(str2)

    if n <= m :
        count = m-n
        

def edit_dist(str1, str2) :
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)] # 2차원 테이블 초기화 

    for i in range(1, n-1) :
        dp[i][0] = 1
    for j in range(1, m-1) :
        dp[0][j] = 1
    '''
    초기설정
        s a t u r d a y
      0 1 2 3 4 5 6 7 8
    s 1
    u 2
    n 3
    d 4
    a 5
    y 6
    '''

    for i in range (1, n+1) :
        for j in range(1, m+1) :
            # 문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if str[i-1] == str[j-1] :
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면 3가지 경우 중에서 최솟값 찾기 -> 여기가 이해가 안된다 정말~
            else :
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1,str2))