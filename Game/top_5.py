player_top5 = []
top5 = []
def player_top(score):
    player_top5.append(score)
    player_top5.sort(reverse=True)
    while len(player_top5) >= 6:
        player_top5.pop()
    return player_top5
def top5(score):
    top5.append(score)
    top5.sort(reverse=True)
    while len(top5) >= 6:
        top5.pop()
    return top5
score = 15
player_top5 = player_top(score)
print(player_top5)
score = 549
player_top5 = player_top(score)
print(player_top5)
score = 69
player_top5 = player_top(score)
print(player_top5)
score = 14
player_top5 = player_top(score)
print(player_top5)
score = 79
player_top5 = player_top(score)
print(player_top5)
score = 89
player_top5 = player_top(score)
print(player_top5)
score = 99
player_top5 = player_top(score)
print(player_top5)
