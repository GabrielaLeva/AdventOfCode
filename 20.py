import re
nodes={}
broadcaster=[]
queue=[]
count_all=[0,0]
class FlipFlop:
    def __init__(self,line) -> None:
        self.name=line[0][1:]
        self.targets=[ i[1:] for i in line[1:] ]
        self.state='off'
    def recieve(self,signal):
        signal=signal[2]
        if signal==0:
            if self.state=='off':
                self.state='on'
                out=1
            else:
                self.state='off'
                out=0
            count_all[out]+=1*len(self.targets)
            queue.extend([(self.name,n,out) for n in self.targets])

class Conjunction:
    def __init__(self,line) -> None:
        self.name=line[0][1:]
        self.targets=[ i[1:] for i in line[1:] ]
        self.inputs={}
    def get_inputs(self):
        for name,node in nodes.items():
            if self.name in node.targets:
                self.inputs[name]=0
    def recieve(self,signal):
        name=signal[0]
        signal=signal[2]
        self.inputs[name]=signal
        out=0 if len(set(self.inputs.values()))==1 and self.inputs[name]==1 else 1
        count_all[out]+=1*len(self.targets)
        queue.extend([(self.name,n,out) for n in self.targets])

with open('20.txt') as file:
    for line in file:
        line=re.findall(r'.\w+',line)
        if line[0][0]=='%':
            nodes[line[0][1:]]=FlipFlop(line)
        elif line[0][0]=='&':
            nodes[line[0][1:]]=Conjunction(line)
        else:
            broadcaster=[ i[1:] for i in line[1:]]

for i in nodes.values():
    if isinstance(i,Conjunction):
        i.get_inputs()
for i in range(1000):
    queue=[('br',i,0) for i in broadcaster]
    for current in queue:
        try:
            nodes[current[1]].recieve(current)
        except KeyError:
            continue
count_all[0]+=(len(broadcaster)+1)*1000
print(count_all[0]*count_all[1])