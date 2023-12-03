total=0
translationTable=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
with open("1.txt") as file:
    for lines in file:
        firstDigit=None
        lastDigit=None
        lines=lines.strip()
        i=0
        while firstDigit is None or lastDigit is None:
            if i>2:
                for id,dig in enumerate(translationTable):
                    firstDigit=id+1 if lines.find(dig,0,i)!=-1 and not firstDigit else firstDigit
                    lastDigit=id+1 if lines.find(dig,(i+1)*-1)!=-1 and not lastDigit else lastDigit
            firstDigit=lines[i] if lines[i].isdigit() and not firstDigit else firstDigit
            lastDigit=lines[(i+1)*-1] if lines[(i+1)*-1].isdigit() and not lastDigit else lastDigit
            i+=1
        total+= int(firstDigit)*10+int(lastDigit)
print(total)
        