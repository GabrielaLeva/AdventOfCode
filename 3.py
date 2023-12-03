import re
total=0
with open("3.txt") as file:
    schema=[line.strip() for line in file.readlines()]
for vertical_i, line in enumerate(schema):
    a=re.search(r'(\d)+',line)
    start=0
    while(a is not None):
        check=''.join([x[max(0,start+a.start()-1):min(len(x),start+a.end()+1)] for x in schema[max(0,vertical_i-1):min(len(schema),vertical_i+2)]])
        for char in check:
            if not char.isdigit() and char!='.':
                total+=int(a.group())
                break
        start+=a.span()[1]
        a=re.search(r'(\d)+',line[start:])
print(total)