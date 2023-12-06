with open('5.txt') as file:
    start= [int(x) for x in file.readline().strip().split()[1:]]
    curr=[]
    for i,x in enumerate (start[::2]):
        curr.extend(range(x,x+start[2*i+1]))
    lock=[True] * len(curr)
    for line in file:
        line=line.strip()
        if line=='':
            continue
        elif line.find("map:")!=-1:
            lock=[True] * len(curr)
            continue
        line=[int(x) for x in line.split()]
        for idx,val in enumerate(curr):
            if val>=line[1] and val<line[1]+line[2] and lock[idx]:
                curr[idx]=val-line[1]+line[0]
                lock[idx]=False
    print(min(curr))