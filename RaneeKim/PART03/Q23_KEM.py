import sys
input = sys.stdin.readline

def reuslt() :
    n = int(input().strip())
    score_list = []
    for _ in range(n) :
        s = list(input().split())
        score_list.append(s)    
    
    score = []
    
    for s in score_list :
        dict_score = {}
        dict_score['name'] = s[0]
        dict_score['korean'] = int(s[1])
        dict_score['english'] = int(s[2])
        dict_score['math'] = int(s[3])
        score.append(dict_score)

    score = sorted(score, key = lambda x : (-x['korean'],x['english'],-x['math'],x['name']))
    for i in range(len(score)) :
        print(score[i]['name'])

    
    return 


reuslt()

