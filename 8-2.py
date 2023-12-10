from math import lcm
map_dict={}
with open("8.txt") as file:
    direcrions=file.readline().strip()
    for line in file:
        line= line.strip()
        map_dict[line[:3]]={"L":line[7:10],"R":line[12:15]}
    dest=[]
    step_table=[]
    for x in map_dict:
        if x[2]=='A':
            dest.append(x)
    for x in dest:
        steps=0
        while steps<100000:
            x=map_dict[x][direcrions[steps%len(direcrions)]]
            steps+=1
            if x[2]=='Z':
                step_table.append(steps)
                break
    print(lcm(*step_table))