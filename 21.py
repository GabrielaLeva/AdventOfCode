steps=64
field=[list(line.strip()) for line in open('21.txt')]
dirs=[(0,-1),(0,1),(1,0),(-1,0)]
for i,line in enumerate(field):
    try:
        start=(line.index('S'),i)
        break
    except ValueError:
        continue
points={start:0}
routes={start:0}
while routes:
    curr_point,step=routes.popitem()
    step+=1
    if step>steps:
        continue
    for dir in dirs:
        new_point=(curr_point[0]-dir[0],curr_point[1]-dir[1])
        if new_point[0]>=0 and new_point[0]<len(field[0]) and new_point[1]>=0 and new_point[1]<len(field) and field[new_point[1]][new_point[0]]=='.' :
            if new_point not in points.keys() or points[new_point]>step:
                points[new_point]=step
                routes[new_point]=step
for curr_point,step in points.items():
    if step%2==0:
        field[curr_point[1]][curr_point[0]]='0'
print(sum([i%2==0 for i in points.values()]))