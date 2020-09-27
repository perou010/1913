from lcr_die import roll_die, stage_for_testing, check_testing

coins = []

def left (coins, player):
    coins[player] -= 1
    if player >=1:
        coins[player-1] += 1
    else:
        coins[player-1] += 1

def right (coins, player):
    coins[player] -= 1
    if player < len(coins)-1:
        coins[player+1] += 1
    else:
        coins[0] += 1


def center (coins, player):
    coins[player] -= 1


def lcr_over(coins):
    uneliminated = 0
    for i in coins:
        if i > 0:
            uneliminated += 1
    if uneliminated > 1:
        return False
    else:
        return True

def lcr_winner(coins):
    for i in range(0, len(coins)):
        if coins[i] > 0:
            return i

def lcr_game(players):
    coins = [3 for i in range(0,players)]
    playerTurn = 0
    coinflips = 1
    roll = ""
    turns = 0

    while lcr_over(coins) == False:

        if coins[playerTurn] <= 3:
            coinflips = coins[playerTurn]
        else:
            coinflips = 3

        while coinflips > 0:
            roll = roll_die()
            if roll == "L":
                left(coins, playerTurn)
            if roll == "R":
                right(coins, playerTurn)
            if roll == "C":
                center(coins, playerTurn)
            coinflips -= 1
        playerTurn += 1
        turns += 1
        if playerTurn > players-1:
            playerTurn = 0
    return(lcr_winner(coins), turns)

def most_common_winner(num_players):
    wins = [0 for i in range(0, num_players)]
    highVal = 0
    valIndex = 0
    for i in range(0, 2000):
        tuple = lcr_game(num_players)
        winner = tuple[0]
        wins[winner] += 1
    for i in range(0, len(wins)):
        if wins[i] > highVal:
            highVal = wins[i]
            valIndex = i
    return(valIndex, highVal/2000)
