import sys
input = sys.stdin.readline

def card_sort() :
    n = int(input().strip())
    card = []
    for i in range(n) :
        card.append(int(input().strip()))

    card = sorted(card)
    sum_s = []
    n = len(card)

    for _ in range(n) :
        if len(card) >=2 :
            card[1] = (card[0] + card[1])
            sum_s.append(card[1])
            del card[0]
            card.sort()    # 최소값을 찾기 위해    
    
    return print(sum(sum_s))

card_sort()
