symbol={
    #x first y second
    "|":{(0,1):(0,1),(0,-1):(0,-1)},
    "-":{(1,0):(1,0),(-1,0):(-1,0)},
    "L":{(0,1):(1,0),(-1,0):(0,-1)},
    "J":{(0,1):(-1,0),(1,0):(0,-1)},
    "F":{(0,-1):(1,0),(-1,0):(0,1)},
    "T":{(0,-1):(-1,0),(1,0):(0,1)},
    ".":{}
}
translation={
    "L":"\\",
    "J":"/",
    "F":"/",
    "T":"\\",
}
field=[]
x,y=(0,0)
with open("10.txt") as file:
    for i,line in enumerate(file):
        line=line.strip()
        field.append(['T' if s=='7' else s for s in line])
        x,y = (line.find('S'),i) if line.find('S')!=-1 else (x,y)
    clean=[ [ '.' for var1 in range(len(line)) ] for var2 in range(i+1) ]
#I find the start manually and see where can it go, yes I am lazy
direction=(-1,0)
clean[y][x]='/'
x+=direction[0]
y+=direction[1]
s=field[y][x]
i=0
while s!='S':
    direction=symbol[s][direction]
    clean[y][x]=translation[s] if s.isalpha() else s
    x+=direction[0]
    y+=direction[1]
    s=field[y][x]
    i+=1
print((i+1)//2)
nest_space=0
for line in clean:
    print(''.join(line))
    prev_corner=None
    edges=0
    for point in line:
        if point=='-':
            continue
        nest_space+=(point=='.')*(edges%2)
        edges+=point=='|'
        if point=='/' or point=='\\':
            if prev_corner is None:
                prev_corner=point
                edges+=1
            elif prev_corner!=point:
                edges+=1
                prev_corner= None
            else:
                prev_corner= None
print(nest_space)