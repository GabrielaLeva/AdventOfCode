import heapq
from math import inf

the_plan=[[int(i) for i in j.strip()] for j in open("17.txt")]
directions=[(0,1),(0,-1),(1,0),(-1,0)]
end=(len(the_plan[0])-1,len(the_plan)-1)


class Vert:
    def __init__(self,point,direct,limit):
        self.point=point
        self.dir=direct
        self.limit=limit
    def as_tuple(self):
        return (self.point,self.dir,self.limit)
    def avail(self):
        direct=directions.copy()
        out=[]
        if self.dir is not None:
            direct.remove((self.dir[0]*-1,self.dir[1]*-1))
            direct.remove(self.dir)
            if self.limit<2:
                out.append(Vert((self.point[0]+self.dir[0],self.point[1]+self.dir[1]),self.dir,self.limit+1))
        for d in direct:
            out.append(Vert((self.point[0]+d[0],self.point[1]+d[1]),d,0))
        return list(filter(lambda x: x.point[0]<=end[0] and x.point[1]<=end[1] and x.point[0]>=0 and x.point[1]>=0,out))
    def ultra(self):
        direct=directions.copy()
        out=[]
        if self.dir is not None:
            direct.remove((self.dir[0]*-1,self.dir[1]*-1))
            direct.remove(self.dir)
            if self.limit<9:
                out.append(Vert((self.point[0]+self.dir[0],self.point[1]+self.dir[1]),self.dir,self.limit+1))
        for d in direct:
            out.append(Vert((self.point[0]+(d[0]*4),self.point[1]+(d[1]*4)),d,3))
        return list(filter(lambda x: x.point[0]<=end[0] and x.point[1]<=end[1] and x.point[0]>=0 and x.point[1]>=0,out))
def ultra_len(dir,start,end):
    match directions.index(dir):
        case 0:
            return sum([arghhh[start[0]] for arghhh in the_plan[start[1]+dir[1]:end[1]+dir[1]]])
        case 1:
            return sum([arghhh[start[0]] for arghhh in the_plan[end[1]:start[1]]])
        case 2:
            return sum(the_plan[start[1]][start[0]+dir[0]:end[0]+dir[0]])
        case 3:
            return sum(the_plan[start[1]][end[0]:start[0]])
def dijkstra(ultra=False):
    start=((0,0),None,0)
    queue=[(0,start)]
    distances={start:0}
    while queue:
        dist, v =heapq.heappop(queue)
        v=Vert(v[0],v[1],v[2])
        if v.point==end:
            return dist
        dirs=v.ultra() if ultra else v.avail() 
        for vert in dirs:
            len_path=dist+the_plan[vert.point[1]][vert.point[0]] if not ultra else dist+ultra_len(vert.dir,v.point,vert.point)
            if len_path<distances.get(vert.as_tuple(),inf):
                distances[vert.as_tuple()]=len_path
                heapq.heappush(queue,(len_path,vert.as_tuple()))
print(dijkstra())
print(dijkstra(ultra=True))