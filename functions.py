from instances import one, two, turn, ABC

def attack(player, pos):
    placed = player.check(pos)
    x = int(pos[0])
    y = int(pos[1])
    print(x)
    print(y)
    if player == one:
        one.other[x][y] = placed
        if placed:
            two.own[x][y] = "x"
        else:
            two.own[x][y] = "o"
    else:
        two.other[x][y] = placed
        if placed:
            one.own[x][y] = "x"
        else:
            one.own[x][y] = "o"


def choosePos():
    attack(one, one.getPosOne())
    attack(two, two.getPosTwo())

def printArrays():
    print("player one")
    for i in one.other:
        print(i)
    print("")
    for i in one.own:
        print(i)
    #
    # print("\n player two")
    # for i in two.other:
    #     print(i)
    # print("")
    # for i in two.own:
    #    print(i)
