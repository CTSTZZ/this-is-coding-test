new_s = ['abc', 'abc', 'abc', 'abc', 'ded', 'ede', 'ded', 'ede','ede']
result_s = []
count = 0
for i in range(len(new_s)-1) :
    if new_s[i] == new_s[i+1] :
        count += 1
    else :
        count += 1
        if count > 1 :
            u = (str(count)+new_s[i])
        else :
            u = new_s[i]
        result_s.append(u)
        count = 0
        print(result_s)  