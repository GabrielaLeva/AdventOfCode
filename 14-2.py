import re
def east(table):
    for i,row in enumerate(table):
        while re.search(r'(O+)(\.+)',row):
            row=re.sub(r'(O+)(\.+)',r'\2\1',row)
        table[i]=row
    return table
def weast(table):
    for i,row in enumerate(table):
        while re.search(r'(\.+)(O+)',row):
            row=re.sub(r'(\.+)(O+)',r'\2\1',row)
        table[i]=row
    return table
def north(table):
    transpose=[''.join([table[j][i] for j in range(len(table))])for i in range(len(table[0]))]
    transpose=weast(transpose)
    return [''.join([transpose[j][i] for j in range(len(transpose))])for i in range(len(transpose[0]))]
def south(table):
    transpose=[''.join([table[j][i] for j in range(len(table))])for i in range(len(table[0]))]
    transpose= east(transpose)
    return [''.join([transpose[j][i] for j in range(len(transpose))])for i in range(len(transpose[0]))]
table=[line.strip() for line in open("14.txt")]
chache_cake=[]
while table not in chache_cake:
    chache_cake.append(table)
    table=north(table)
    table=weast(table)
    table=south(table)
    table=east(table)
first_occurance=chache_cake.index(table)
chache_cake=chache_cake[chache_cake.index(table):]
table=chache_cake[(1000000000-first_occurance)%len(chache_cake)]
the_length=len(table)
total=0
for i,row in enumerate(table):
    ohs=re.finditer(r'O+',row)
    for j in ohs:
        total+=(j.end()-j.start())*(the_length-i)
print(total)