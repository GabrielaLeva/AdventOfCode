visited=['']
tiles=[x.strip() for x in open("16.txt")]
visited=[['.' for i in tiles[0]] for j in tiles]
class Beam:
    def __init__(self,pos_x,pos_y,dir_x,dir_y) -> None:
        self.x=pos_x
        self.y=pos_y
        self.dir_x=dir_x
        self.dir_y=dir_y
        self.tile=tiles[pos_y][pos_x]
    def move(self):
        self.x+=self.dir_x
        self.y+=self.dir_y
        self.tile=tiles[self.y][self.x]
    def rotate(self,twist):
        self.dir_x,self.dir_y=self.dir_y*twist,self.dir_x*twist
    def split(self):
        self.rotate(1)
        return Beam(self.x,self.y,self.dir_x*-1,self.dir_y*-1)
beams=[Beam(0,0,1,0)]
symbols={'-':[(0,1),(0,-1)],
         '|':[(1,0),(-1,0)],
         '/':-1,
         '\\':1,
         '.':[]
         }
while len(beams)>0:
    for beam in beams:
        try:
            if beam.x<0 or beam.y<0:
                raise IndexError
            instruct=symbols[beam.tile]
            if type(instruct) is int:
                beam.rotate(instruct)
            elif (beam.dir_x,beam.dir_y) in instruct:
                beams.append(beam.split())
            check_energised=visited[beam.y][beam.x]
            if check_energised=='.':
                visited[beam.y][beam.x]='-' if beam.dir_x!=0 else '|'
            elif beam.tile=='.' and (check_energised=='+' or (beam.dir_x,beam.dir_y) not in symbols[check_energised]):
                beams.remove(beam)
                continue
            else:
                visited[beam.y][beam.x]='+'
            beam.move()
        except IndexError:
            beams.remove(beam)
[print(''.join(i)) for i in visited]
print(len(visited)*len(visited[0])-sum([i.count('.') for i in visited]))