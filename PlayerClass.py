import random

position = (random.randint(0, 7), random.randint(0, 7))

class player():
    def __init__(self, own):
        self.size = 10
        self.ships = [(2, 1), (3, 1), (4, 1), (5,1), (5,2)]
        self.own = own

        self.enemyAttacks = []

        self.other =   [[None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None]]

    def check(self, pos):
        if self.own[int(pos[0])][int(pos[1])]:
            return True
        else:
            return False

    def getPosOne(self):
        print("Wehere do you want to attack? (i.e.: (1, 5)) ")
        position = input()
        while int(position[0]) > 7 or int(position[1]) > 7:
            print("Index out of bounce. Highest possible index is 7. ")
            position = input()
        return position

    def getPosTwo(self):
        global position
        while position in self.enemyAttacks:
            posX = random.randint(0, 7)
            posY = random.randint(0, 7)
            position = (posX, posY)
        self.enemyAttacks.insert(-1, position)
        return position
