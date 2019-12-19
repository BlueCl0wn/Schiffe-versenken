import random

class player():
    def __main__(self, own):
        self.size = 10
        self.ships = [(2, 1), (3, 1), (4, 1), (5,1), (5,2)]

        self.own = own

        self.other =   [[none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none],
                        [none, none, none, none, none, none, none, none, none, none]]

    def check(self, pos):
        if own[pos[0]][pos[1]]:
            return true
        else:
            return false

    def getPosOne(self):
        print("We=here do you want to attack? (i.e.: (A, 5)) ")
        position = input
        return position

    def getPosTwo(self):
        posX = random.choice(ABC)
        posY = random.randint(0, 7)
        position = (posX, posY)
        return position
