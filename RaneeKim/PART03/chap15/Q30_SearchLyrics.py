words = ['frodo','front','frost','frozen','frame','kakao']
queries = ['fro??','????o','fr???','fro???','pro?']
queries_list = [[e for e in i] for i in queries]
words_list = [[e for e in i] for i in words]

answer = []
for queryy in queries_list :
    count = 0
    for word in words_list :
        if len(word) == len(queryy) :
            cheak_index = []
            for i in range(len(queryy)) :
                if queryy[i] != '?' :
                    cheak_index.append(i)
            count_2 = 0
            for c in cheak_index :
                if word[c] == queryy[c] :
                    count_2 += 1
            if count_2 == len(cheak_index) :
                count += 1
    answer.append(count)
