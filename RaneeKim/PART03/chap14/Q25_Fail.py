import sys
input = sys.stdin.readline

def fail() :
    n = int(input().strip())
    stages = sorted(list(map(int, input().split())))
    
    stages_fail = []
    m = max(stages)

    for i in range(1,m+1) :
        fail = {}
        count = 0

        if i != n+1 :
            for u in range(len(stages)) :
                if i not in(stages) :
                    fail['stage'] = i
                    fail['fail_p'] = 0           
                    break
                elif i == stages[u] :
                    count += 1
                                    
            fail['stage'] = i
            fail['fail_p'] = count/len(stages)
            del stages[0:count]
                
            stages_fail.append(fail)   
    
    stages_fail = sorted(stages_fail, key=lambda x : -x['fail_p'])
    result = [stages_fail[i]['stage'] for i in range(len(stages_fail))]
    
    return result

fail()


def answer() :
    n = int(input().strip())
    stages = sorted(list(map(int, input().split())))

    fail_len = len(stages)
    fail_result = []

    for i in range(1,n+1) :
        count = stages.count(i) 
        # stages 리스트 안에서 값이 i인것을 카운트해라
        # i번째 stage에서 탈락한 자를 카운트하는 것

        if count == 0 :
            fail = 0
        else :
            fail = count/fail_len
        
        fail_result.append([i,fail])
        fail_len -= count 
        # 탈락한 참가자 수 만큼 빼가는 것
        # 1,2,3 오름차순 단계별로 사람이 탈락하기에 가능함

    fail_result = sorted(fail_result, key = lambda x : -x[1])
    result = [i[0] for i in fail_result]

    return result
    
