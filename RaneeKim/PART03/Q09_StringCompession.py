import sys
input = sys.stdin.readline

def string() :
    s = input().strip()
    final = []
    for i in range(1,(len(s)//2)+1) :
        cheak = []
        while_cheak = 0
        start = 0
        while while_cheak <= len(s)//i :
            cheak.append(s[start:start+i])
            start += i
            while_cheak += 1
        final.append(cheak) 
        # [['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c', ''], 
        # ['aa', 'bb', 'ac', 'cc', ''], ['aab', 'bac', 'cc'], ['aabb', 'accc', '']]

    final_result = []
    for f in final :
        count = 1
        result = ''        
        for j in range(len(f)) :
            try :
                word_1 = f[j]
                word_2 = f[j+1]
                if word_1 == word_2 :
                    count += 1
                else :
                    if count == 1  :
                        result += word_1 
                    else :
                        result += (str(count)+word_1)
                    count = 1
            except :
                pass
        result += f[-1]
        final_result.append(len(result))

    return min(final_result)

string()

'''
aabbaccc
ababcdcdababcdcd
abcabcdede
abcabcabcabcdededededede
xababcdcdababcdcd
'''

'''
def string() :
    s = input().strip()
    final_result = []
    for i in range(1,(len(s)//2)+1) :
        string_count = 1
        while_count = 0
        start = 0
        cheak = (len(s) // i) - 1
        result = ''
        while while_count != cheak :
            if s[start:start+i] == s[start+i:start+i+i] :
                string_count += 1
                while_count += 1
                start += i
            else :

                if string_count != 1 : 
                    result += (str(string_count) + s[start:start+i])
                else :
                    result += s[start:start+i]
                
                string_count = 1
                while_count += 1
                start += i
            
        if len(s) % i == 0 :
            result +=  (str(string_count)+s[-(i):])
        elif len(s) % i > 0 :
            result += s[-(len(s)%i):]
        
        final_result.append(len(result))
        print(result)
    return final_result

string()
'''

'''
def solution(s):
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
        new_s.append("ㄱ") # ['abc', 'abc', 'abc', 'abc', 'ded', 'ede', 'ded', 'ede','ㄱ']

        count = 0
        result_s = [] 
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
      

        count_result = ''
        for i in result_s :
            count_result += i

        result.append(len(count_result))
    return min(result)



S = "abcabcabcabcdededededede" 
def solution(S)
'''