pp = '

def good_balance(p): #  균형이 딱 맞을때의 index값을 뽑아냄 
    count = 0 
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i
        

def check(p) :
    count = 0
    for i in p :
        if i == '(' :
            count += 1
        else :
            if count == 0 :
                return False # 쌍이 맞지않을때는
            count -= 1
    return True



def solution(p) : \
    
    # p = '))(( ()' 
    answer = ''
    if p == '' :
        return answer
    index = good_balance(p)  # 
    u = p[:index+1] # 발란스가 맞는 부분 ))((
    v = p[index+1:] # 그 뒷부분 ()

    if check(u) : 
        answer = u + solution(v) #
        # real_answer = () +  slountion[ ))((() ] = (())()
        # ()(())()
    else : # 재귀함수가 돌아갔을 때 u = ))((, v = ()
        answer = '('
        answer += solution(v) # ( +  ()
        answer += ')' # ( +  () + )
        u = list(u[1:-1]) # 첫번째 마지막 문자 제거 -> )(  
        for i in range(len(u)) : 
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '(' # ()
        answer += "".join(u)  # (())()
    return answer



solution(pp) 