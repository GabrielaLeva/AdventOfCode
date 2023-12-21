import re
from collections import namedtuple
minmaxpair=namedtuple("minmaxpair",['min','max'])
start=minmaxpair(1,4000)
queue=[{'x':start,'m':start,'a':start,'s':start,'state':'in'}]
accepted=[]
class StateSwitcher:
    todo='i need to code this up'
    def __init__(self,list) -> None:
        conds=[]
        for a in list[:-1]:
            a=re.match(r'([xmas])([<>])(\d+):(\w+)',a).groups()
            pair=minmaxpair(1,int(a[2])-1) if a[1]=='<' else minmaxpair(int(a[2])+1,4000)
            conds.append({'pair':pair,'xmas?':a[0],'state':a[3]})            
        self.conditions=conds
        self.default_state=list[-1]
    def check(self,toy_dict:dict) ->str:
        for c in self.conditions:
            pair,letter,state=c.values()
            if pair.min==1:
                if toy_dict[letter].min>pair.max:
                    continue
                elif toy_dict[letter].max<=pair.max:
                    toy_dict['state']=state
                    break
                else:
                    out=toy_dict.copy()
                    out[letter]=minmaxpair(toy_dict[letter].min,pair.max)
                    out['state']=state
                    queue.append(out)
                    toy_dict[letter]=minmaxpair(pair.max+1,toy_dict[letter].max)
            else:
                if toy_dict[letter].max<pair.min:
                    continue
                elif toy_dict[letter].min>=pair.min:
                    toy_dict['state']=state
                    break
                else:
                    out=toy_dict.copy()
                    out[letter]=minmaxpair(pair.min,toy_dict[letter].max)
                    out['state']=state
                    queue.append(out)
                    toy_dict[letter]=minmaxpair(toy_dict[letter].min,pair.min-1)
        else:
            toy_dict['state']=self.default_state
states={}
total=0
with open('19.txt') as file:
    separator=True
    for line in file:
        line = line.strip()
        if line == '':
            break
        line=line.split('{')
        line[1]=line[1][:len(line[1])-1].split(',')
        states[line[0]]=StateSwitcher(line[1])
while queue:
    working=queue.pop(0)
    while working['state'] !='A' and working['state'] !='R':
        print(working['state'],(working['x'].max-working['x'].min+1)*(working['m'].max-working['m'].min+1)*(working['a'].max-working['a'].min+1)*(working['s'].max-working['s'].min+1))
        states[working['state']].check(working)
    if working['state'] =='A':
        del working['state']
        print(working)
        res=1
        for pair in working.values():
            res*=pair.max-pair.min+1
        print(res)
        total+=res
print(total)