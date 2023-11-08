n = int(input())
s_point = list(map(int, input().split()))

s_point.sort()
count = 0
team = []

for s in s_point : 
    if len(team) <= s : # s이하를 사용한 이유는 team안에 s공포도를 가진 그 사람이 들어가야 되기 때문
        team.append(s)
    if len(team) >= s : # s이상을 사용한 이유는 team에 s공포도만큼 조원수가 s라면 다음 조를 만들어야 하기 때문
        team=[]
        count +=1 # team이 만들어졌을 때 count수 올라감

# 문제해결포인트 : 몇몇 인원은 버려도된다 -> 공포심이 제일 큰 조원이 조가 불가능하다면 버려도 된다

print(count)

'''
[1]
1
[2]
[2, 2]  
2
[2]
[2, 2] # S이상을 사용한 이유에 대한 세부 설명
3
[2] # 공포도가 2기 때문에 인원이2명인 조로 편입할 수 있지만 다음 공포도가 큰 3을 위해 다음 팀으로 넘어가야함
[2, 3]
[2, 3, 3]   # 여기까지
4
[4]
[4, 4]
[4, 4, 4]
[4, 4, 4, 5]
[4, 4, 4, 5, 5]
5
[7]
'''