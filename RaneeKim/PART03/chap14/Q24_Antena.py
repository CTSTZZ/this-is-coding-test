import sys
input = sys.stdin.readline

def result() :
    n = int(input().strip())
    antena = list(map(int, input().split()))

    antena_sum = []
    for i in antena :
        c = 0
        antena_dict = {}
        for e in antena :
           c += abs(i-e)
        antena_dict['house_num'] = i
        antena_dict['sum'] = c
        antena_sum.append(antena_dict)
    
    antena_sum = sorted(antena_sum, key = lambda x : (x['sum'], x['house_num'])) # sum이같을때 house_num으로 한번더  sort 넣어야함
    print(antena_sum[0]['house_num']) 

    return

result()


def answer() :
    n = int(input().strip())
    antena = sorted(list(map(int, input().split())))

    result = antena[(n-1)//2] # 중간값 찾는거
    return result