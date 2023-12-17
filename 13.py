def find_symetry(matrix):
    candidates=[]
    for i in range(1,len(matrix)):
        if matrix[i]==matrix[i-1]:
            candidates.append(i)
    sym_lines=candidates.copy()
    for candidate in candidates:
        limit=min(candidate,len(matrix)-candidate)
        a=matrix[candidate:candidate+limit]
        a.reverse()
        if a!=matrix[candidate-limit:candidate]:
            sym_lines.remove(candidate)
    return 0 if len(sym_lines)==0 else sym_lines[0]
def off_by_one_letter(str1,str2):
    rez=0
    for i,letter in enumerate(str1):
        if letter!=str2[i]:
            idx=i
            rez+=1
    return idx if rez==1 else -1
def odd_one(matrix):
    key=list(set(matrix))
    pattern=[key.index(x) for x in matrix]
    for i in range(1,len(pattern)):
        part=pattern[i:i+i]
        part.reverse()
        second=pattern[i-len(part):i]
        possible_smudge=off_by_one_letter(second,part)
        if possible_smudge!=-1 and off_by_one_letter(key[part[possible_smudge]],key[second[possible_smudge]])!=-1:
            return i
    return 0
mirror_list=[]
total,total2=(0,0)
with open("13.txt") as file:
    for line in file:
        line=line.strip()
        if line=="":
            transpose=[''.join([mirror_list[j][i] for j in range(len(mirror_list))])for i in range(len(mirror_list[0]))]
            temp=find_symetry(mirror_list)*100 
            temp=temp if temp!=0 else find_symetry(transpose)
            total+=temp
            temp=odd_one(mirror_list)*100
            temp=temp if temp!=0 else odd_one(transpose)
            total2+=temp
            mirror_list=[]
        else:
            mirror_list.append(line)
print(total,total2)