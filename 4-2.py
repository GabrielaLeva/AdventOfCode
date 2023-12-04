total=0
with open('4.txt') as file:
    pseudo_queue=[0]
    for line in file:
        score=0
        try:
            amount=pseudo_queue.pop(0)+1
        except IndexError:
            amount=1
        total+=amount
        nums=line[line.index(":"):line.index("|")].strip().split()
        winning=line[line.index("|"):].strip().split()
        for num in nums:
            if num in winning:
                score+=1
        for idx in range(score):
            if idx<len(pseudo_queue):
                pseudo_queue[idx]+=amount
            else:
                pseudo_queue.append(amount)
print(total)