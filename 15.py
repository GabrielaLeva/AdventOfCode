import re
a= open("15.txt").readline()
a=a.strip().split(',')
boxess=[[] for i in range(256)]
total=0
for lens in a:
    atts=re.match(r'(\w+)(=|\-)(\d*)',lens)
    lable,operation,value= atts.groups()
    hashbrown=0
    for char in lable:
        hashbrown=((hashbrown+ord(char))*17)%256
    if operation=='-':
        for i in boxess[hashbrown]:
            if i[0]==lable:
                boxess[hashbrown].remove(i)
    else:
        for idx,i in enumerate(boxess[hashbrown]):
            if i[0]==lable:
                boxess[hashbrown][idx]=(lable,value)
                break
        else:
            boxess[hashbrown].append((lable,value))
for i,box in enumerate(boxess):
    for idx,lens in enumerate(box):
        total+=(i+1)*(idx+1)*int(lens[1])
print(total)