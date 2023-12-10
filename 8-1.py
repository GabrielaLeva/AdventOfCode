map_dict={}
with open("8.txt") as file:
    direcrions=file.readline().strip()
    for line in file:
        line= line.strip()
        map_dict[line[:3]]={"L":line[7:10],"R":line[12:15]}
    dest='AAA'
    steps=0
    while dest!='ZZZ':
        dest=map_dict[dest][direcrions[steps%len(direcrions)]]
        steps+=1
    print(steps)