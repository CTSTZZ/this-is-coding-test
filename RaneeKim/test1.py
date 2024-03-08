def solution(babblings):
    answer = 0    
    for babbling in babblings :
        cheak = ''
        result = 0
        for i in babbling :
            cheak += i
            if cheak in ["aya", "ye", "woo", "ma"] :
                    result += len(cheak)
                    cheak = ''
        if len(babbling) == result :
            answer += 1                
    return answer
