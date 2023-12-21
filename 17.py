directions=[(0,1),(0,-1),(1,0),(-1,0)]
the_plan=[[int(i) for i in j.strip()] for j in open("17.txt")]
class Pathy_ms_pathface:
    def __init__(self,point,direct,limit,parent):
        self.point=point
        self.direct=direct
        self.limit=limit
        self.steps=the_plan[self.point[1]][self.point[0]]
        self.parent=parent
    def update_parent(self,new_parent):
        if new_parent.distance()+self.steps<self.distance():
            self.parent=new_parent
    def movable(self,direct):
        if direct[0]==-1*self.direct[0] and direct[1]==-1*self.direct[1]:
            return False
        elif self.direct==direct and self.limit>3:
            return False
        else:
            return True
    def distance(self):
        return 0 if self.parent is None else self.parent.distance()+self.steps
priority=[Pathy_ms_pathface((0,0),(0,0),0,None)]
end=(len(the_plan[0])-1,len(the_plan)-1)
def in_priority(point):
    for i,elem in enumerate(priority):
        if elem.point==point:
            return i
    return -1
print(the_plan)
def dijkstra():
    while priority:
        i=priority.pop(0)
        print(i.point,i.distance())
        for d in directions:
            if i.movable(d):
                try:
                    new_limit=i.limit+1 if i.direct==d else 0
                    new_point=(i.point[0]+d[0],i.point[1]+d[1])
                    if new_point[0]<0 or new_point[1]<0:
                        continue
                    elem=in_priority(new_point)
                    val=the_plan[new_point[1]][new_point[0]]
                    if elem!=-1:
                        priority[elem].update_parent(i)
                    elif new_point==end:
                        return i.distance()+val
                    else:
                        priority.append(Pathy_ms_pathface(new_point,d,new_limit,i))
                except IndexError:
                    continue
        priority.sort(key=lambda x:x.distance())
print(dijkstra())