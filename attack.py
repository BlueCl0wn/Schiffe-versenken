from instances import one, two, turn, ABC

def attack(player, pos):
    placed = player.check(pos)
    if player == one:
        two.other[pos[0]][pos[1]] = placed
    else
        one.other[pos[0]][pos[1]] = placed
    turn = 1

def choosePos(turn):
    if not turn:
        one.getPosOne()
        turn = 1
    else:
        two.getPosTwo()
        turn = 0
