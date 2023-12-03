total=0
with open("3.txt") as file:
    schema=[line.strip() for line in file.readlines()]
for vertical_i, line in enumerate(schema):
    try:
        idx=line.index('*')
        while 1:
            parts=0
            ratio=1
            parray=[]
            for x in schema[max(0,vertical_i-1):min(len(schema),vertical_i+2)]:
                i=idx-1
                while i<idx+2:
                    if x[i].isdigit():
                        end=x.find('.',i)
                        end= end if end !=-1 else len(x)+2
                        if x[idx]=='*':
                            a=x[x.rfind('.',0,idx)+1:idx] if x[x.rfind('.',0,idx)+1:idx]!='' else '1'
                            b=x[idx+1:end] if x[idx+1:end]!='' else '1'
                            ratio*=int(a)
                            ratio*=int(b)
                            parray.append(a)
                            parray.append(b)
                            if a=='1' or b=='1':
                                parts+=1
                            else:
                                parts+=2
                            break
                        parts+=1
                        parray.append(x[x.rfind('.',0,i)+1:end])
                        ratio*=int(x[x.rfind('.',0,i)+1:end])
                        i=end
                    else:
                        i+=1
            print('gear',vertical_i,idx,'parts',parray)
            total+=ratio if parts == 2 else 0
            idx=line.index('*',idx+2)
    except ValueError:
        continue
print(total)