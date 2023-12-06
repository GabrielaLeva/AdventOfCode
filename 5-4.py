with open('5.txt') as file:
    the_level=[0]
    lookup_dict={0:0}
    line=file.readline().strip().split()[1:]
    points=[[int(x),int(x)+int(line[i*2+1])] for i,x in enumerate(line[::2])]
    for line in file:
        line=line.strip()
        if line=='':
            continue
        elif line.find("map:")!=-1:
            the_level.sort()
            the_level = [i for n, i in enumerate(the_level) if i not in the_level[:n]] 
            for i,point in enumerate(points):
                for ranges in range(len(the_level)-1):
                    if the_level[ranges]<=point[0] and point[0]<the_level[ranges+1]:
                        if the_level[ranges+1]<point[1]:
                            points.append([the_level[ranges+1],point[1]])
                            points[i][1]=the_level[ranges+1]
                        points[i][0]+=lookup_dict[the_level[ranges]]
                        points[i][1]+=lookup_dict[the_level[ranges]]
                        break
            print(the_level,lookup_dict,points)
            the_level=[0]
            lookup_dict={0:0}
            continue
        line=[int(x) for x in line.split()]
        the_level.append(line[1])
        the_level.append(line[1]+line[2])
        lookup_dict[line[1]]=line[0]-line[1]
        if line[1]+line[2] not in lookup_dict.keys():
            lookup_dict[line[1]+line[2]]=0
the_level.sort()
the_level = [i for n, i in enumerate(the_level) if i not in the_level[:n]] 
for i,point in enumerate(points):
    for ranges in range(len(the_level)-1):
        if the_level[ranges]<=point[0] and point[0]<the_level[ranges+1]:
            if the_level[ranges+1]<point[1]:
                points.append([the_level[ranges+1],point[1]])
                points[i][1]=the_level[ranges+1]
            points[i][0]+=lookup_dict[the_level[ranges]]
            points[i][1]+=lookup_dict[the_level[ranges]]
            break
print(the_level,lookup_dict,points)
print(min([x[0] for x in points]))