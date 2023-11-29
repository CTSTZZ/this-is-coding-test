import sys
input = sys.stdin.readline

def card_sort() :
    n = int(input().strip())
    card = []
    for _ in range(n) :
        card.append(int(input().strip()))

    card = sorted(card)
    sum_s = []
    n = len(card)

    for _ in range(n) :
        if len(card) >= 2 :
            card[1] = (card[0] + card[1]) # 50 40 45 50 
            # 100
            sum_s.append(card[1]) # 50, 95, 100, 185
            del card[0]
            card.sort() # 얘가 팁이구나,,
    
    return print(sum(sum_s))

card_sort()


