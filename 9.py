def extrapolate(seq,backward):
    differances=[]
    times=1 if backward==0 else -1
    for i in range(len(seq)-1):
        differances.append(seq[i+1]-seq[i])
    return seq[-1+backward]+extrapolate(differances,backward)*times if len(set(differances))!=1 else seq[-1+backward]+differances[0]*times
total,total2=0,0
with open("9.txt") as file:
    for sequence in file:
        total+=extrapolate([int(x) for x in sequence.strip().split()],0)
        total2+=extrapolate([int(x) for x in sequence.strip().split()],1)
print(total,total2)