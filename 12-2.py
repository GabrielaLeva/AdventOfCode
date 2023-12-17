import re
from math import factorial
with open("12.txt") as file:
    total=0
    for line in file:
        schema,numbers=line.strip().split()
        schema='?'.join([schema for j in range(5)])
        nfa_states=['.']
        working_states=[1]
        working_states.extend([0]*len(nfa_states))
        numbers=[int(x) for x in numbers.split(',')]
        for j in range(5):
            for x in numbers:
                for i in range(x):
                    nfa_states.append('#')
                nfa_states.append('.')
        for x in schema:
            new_states=[0]*len(nfa_states)
            for state in range(len(working_states)):
                match x:
                    case '.':
                        if state + 1 < len(nfa_states) and  nfa_states[state+1]=='.':
                            new_states[state+1]+=working_states[state]
                        if nfa_states[state]=='.':
                            new_states[state]+=working_states[state]
                    case '?':
                        if state + 1 < len(nfa_states):
                            new_states[state + 1] += working_states[state]
                        if nfa_states[state] == ".":
                            new_states[state] += working_states[state]
                    case '#':
                        if state + 1 < len(nfa_states) and nfa_states[state+1]=='#':
                            new_states[state+1]+=working_states[state]
            working_states=new_states
        total+=sum(working_states[:-3:-1])
    print(total)