import random

def roll():
    val=random.randint(1,6)
    return val

while True:
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else :
            print("Number of player should be between 2 to 4")
    else:
        print("Enter a valid input")

player_scores = [0 for _ in range(players)]

while max(player_scores)<50:
    for i in range(players):
        print(f"player {i+1}, your turn has just started")
        print(f"Your current score is {player_scores[i]}")
        current_score=0
        while True:
            ch=input("Do you want to roll(y)? ")
            if ch.lower()!='y':
                break
            value=roll()
            print(f"You have rolled a {value}")
            if value!=1:
                current_score+=value
            else:
                print("Your turn is over")
                current_score=0
                break
        player_scores[i]+=current_score
        print(f"player {i+1}, your new score is {player_scores[i]}")


print(f"The winner is player {player_scores.index(max(player_scores)) + 1} with a score of {max(player_scores)}")