num_values={
    "A":13,
    "K":12, 
    "Q":11, 
    "T":10,
    "J":1, 
}
games={
    "high_card":[],
    "pair":[],
    "pairs":[],
    "three_of_kind":[],
    "full_house":[],
    "four_of_kind":[],
    "five_of_kind":[]
}
promotion={
    "high_card":"pair",
    "pair":"three_of_kind",
    "pairs":"full_house",
    "three_of_kind":"four_of_kind",
    "full_house":"five_of_kind",
    "four_of_kind":"five_of_kind",
    "five_of_kind":"five_of_kind"
}
total=0
counter=1
def get_value(obj):
    return obj["value"]
with open("7.txt") as file:
    for game in file:
        game = game.strip().split()
        original=[int(x) if x.isdigit() else num_values[x] for x in game[0]]
        sorted_cards=sorted(original)
        lable="high_card"
        value=0
        if sorted_cards[0]==sorted_cards[4]:
            lable="five_of_kind"
        elif sorted_cards[0]==sorted_cards[3] or sorted_cards[1]==sorted_cards[4]:
            lable="four_of_kind"
        elif (sorted_cards[0]==sorted_cards[2] and sorted_cards[3]==sorted_cards[4]) or (sorted_cards[0]==sorted_cards[1] and sorted_cards[2]==sorted_cards[4]):
            lable="full_house"
        else:
            for idx,card in enumerate(sorted_cards):
                if idx==4:
                    break
                if idx+2<5 and card==sorted_cards[idx+2] and card!=1:
                    lable="three_of_kind"
                    break
                elif card==sorted_cards[idx+1] and card!=1:
                    if lable=="pair":
                        lable+='s'
                        break
                    else:
                        lable="pair"
        for i in sorted_cards:
            if i!=1 or lable=="five_of_kind":
                break
            lable=promotion[lable]
        for i in original:
            value=value*100+i
        games[lable].append({"bid":int(game[1]),"ordering":sorted_cards,"value":value})
for rank in games:
    all_of_rank=games[rank]
    all_of_rank.sort(key=get_value)
    while len(all_of_rank)>0:
        print(all_of_rank[0]["ordering"],counter,rank)
        total+=all_of_rank.pop(0)["bid"]*counter
        counter+=1

print(total)
