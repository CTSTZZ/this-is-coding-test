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


