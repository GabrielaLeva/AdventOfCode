currpoint=[0,0]
points=[[0,0]]
area=[0,0]
control=0
dirs_dirs=['R','D','L','U']
dirs={'U':(0,-1),
      'D':(0,1),
      'R':(1,0),
      'L':(-1,0)}
with open("18.txt") as file:
    for first_two,line in enumerate(file):
        color=line.strip().split()[2]
        amount=int(color[2:7],base=16)
        direction=dirs[dirs_dirs[int(color[7])]]
        currpoint=[cord+direction[i]*amount for i,cord in enumerate(currpoint)]
        control+=amount
        points.append(currpoint)
        print(color)
for i in range(len(points)-1):
    area[0]+=points[i][0]*points[i+1][1]
    area[1]+=points[i][1]*points[i+1][0]
print((area[0]-area[1]+control)//2+1)