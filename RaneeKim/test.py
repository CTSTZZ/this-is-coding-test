
left,right,offset = map(int, input().split())
offset_1 = list(map(int, str(offset+1)))
offset_2 = list(map(int, str(offset+2)))   
offset = list(map(int, str(offset)))
 

nnum = []
count = 0
while count < len(offset) :
    if offset[count] != 1 :
        a = offset[count]
        count += 1
    else :
        a = str(offset[count]) + str(offset[count+1])
        count += 2
    nnum.append(a)

count = 0
while count < len(offset_1) :
    if offset_1[count] != 1 :
        a = offset_1[count]
        count += 1
    else :
        a = str(offset_1[count]) + str(offset_1[count+1])
        count += 2
    nnum.append(a)

count = 0
while count < len(offset_2) :
    if offset_2[count] != 1 :
        a = offset_2[count]
        count += 1
    else :
        a = str(offset_2[count]) + str(offset_2[count+1])
        count += 2
    nnum.append(a)
    
nnum = list(map(int, nnum))

switch = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
b = ''
for i in nnum :
    b += switch[i]
        
answer = b[10:20]


solution(10,20,210)