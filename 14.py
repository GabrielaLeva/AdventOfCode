import re
total=0
table=[line.strip() for line in open("14.txt")]
transpose=[''.join([table[j][i] for j in range(len(table))])for i in range(len(table[0]))]
the_length=len(table)
for i in table:
    print(i)
for row in transpose:
    stones=[0]
    stones.extend([i.end() for i in re.finditer(r'#+',row)])
    for i,str in enumerate(re.split(r'#+',row)):
        iter=0
        for j in str:
            if j=="O":
                total+=the_length-stones[i]-iter 
                iter+=1
print(total)