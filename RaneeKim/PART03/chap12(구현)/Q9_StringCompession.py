s = "abcabcabcabcdededededede" # 24

result = []
for i in range(1,len(s)+1):
    new_s = []
    n = 0
    c = i
    for _ in range(len(s)//i) : # i = 1, for문은 0~시작함 -> 12번만큼 돌아간다고해,,
        new_s.append(s[n:c])  #  0~2
        n += i
        c += i
        if c > len(s) :
            c = len(s)
            if s[n:c] != "" : # len(s)/i 가 나머지가 0일때는 리스트배열이 공백으로 마지막에 추가되는 것을 방지하기위하여
                new_s.append(s[n:c])
    count = 0
    result_s = [] # ['abc', 'abc', 'abc', 'abc', 'ded', 'ede', 'ded', 'ede']
    for i in range(1,len(new_s)) :
        if new_s[i] == new_s[i-1] :
            count += 1
        else :
            count += 1
            if count > 1 :
                u = (str(count)+new_s[i-1])
            else :
                u = new_s[i-1]
            result_s.append(u)
            count = 0
            print(result_s)         
    result.append(len(result_s))
    

min(result)