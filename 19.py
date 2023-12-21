import re
def lamdaifier(paramstr):
    if paramstr[1]=='>':
        return lambda x:paramstr[3] if x[paramstr[0]]>int(paramstr[2]) else False
    else:
        return lambda x:paramstr[3] if x[paramstr[0]]<int(paramstr[2]) else False
class StateSwitcher:
    def __init__(self,list) -> None:
        lambdas=[]
        for a in list[:-1]:
            a=re.match(r'([xmas])([<>])(\d+):(\w+)',a)
            lambdas.append(lamdaifier(a.groups()))            
        self.conditions=lambdas
        self.default_state=list[-1]
    def check(self,toy_dict) ->str:
        out=''
        i=0
        while not out and i<len(self.conditions):
            out=self.conditions[i](toy_dict)
            i+=1
        return out if out else self.default_state
    def __str__(self) -> str:
        return " ".join(self.conditions)
states={}
total=0
with open('19.txt') as file:
    separator=True
    for line in file:
        line = line.strip()
        if line == '':
            separator=False
        elif separator:
            line=line.split('{')
            line[1]=line[1][:len(line[1])-1].split(',')
            states[line[0]]=StateSwitcher(line[1])
        else:
            line={a[0]:int(a[2:]) for a in line[1:-1].split(',')}
            next_state='in'
            while next_state not in ['A','R']:
                next_state=states[next_state].check(line)
            total+=0 if next_state=='R' else sum(line.values())
print(total)