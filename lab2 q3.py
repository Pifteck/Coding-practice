from operator import itemgetter
players = [("Anna",18,70),("John",20,80),("Jony",19,95),("Json",23,120)]
sort_players = sorted(players,  key=itemgetter(0))
print(sort_players)