colors=['r','g','b']
total=0
with open("2.txt") as file:
    for line in file:
        maxes=[0,0,0]
        line=line.strip().split()
        id=int(line[1][:-1])
        amounts=[int(x) for x in line[2::2] ]
        color=[x[0] for x in line[3::2]]
        for i,cubes in enumerate(color):
            if maxes[colors.index(cubes)]<amounts[i]:
                maxes[colors.index(cubes)]=amounts[i]
        total+=maxes[0]*maxes[1]*maxes[2]
print(total)