total=0
with open('4.txt') as file:
    for line in file:
        score=0
        nums=line[line.index(":"):line.index("|")].strip().split()
        winning=line[line.index("|"):].strip().split()
        for num in nums:
            if num in winning:
                score=score*2 if score!=0 else 1
        total+=score
print(total)