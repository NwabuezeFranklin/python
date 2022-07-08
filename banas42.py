import math
import random

class warrior:
    def __init__(self, name="", attack=0, block=0, health=0):
        self.name = name
        self.attack = attack
        self.block = block
        self.health = health
    def attacker(self):
        attackgenerator = self.attack * random.randint(0,2)
        return attackgenerator
    def blocker(self):
        blockergen = self.block * random.randint(0,1)
        return blockergen
class Battle:
    def startfigth(self, war1, war2):
        while True:
            if self.getresult(war1,war2) == "Game Over":
                print("Game Over")
                break
            if self.getresult(war2,war1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getresult(warA,warB):
        warAAttack = warA.attacker()
        warBBlock = warB.blocker()
        warADamage = warAAttack - warBBlock
        if warBBlock > warAAttack:
            warADamage = 0
        warB.health = warB.health - warADamage
        print("{} attacks and deals {} damage to {}".format(warA.name,warADamage,warB.name))
        print("{} is down to {} health".format(warB.name, warB.health))
        if warB.health <= 0:
            print("{} died and {} is Victorious".format(warB.name, warA.name))
            return "Game Over"
        else:
            return "Fight"

def main():
    l = warrior("Rick", 100,50,300)
    s = warrior("Morty",85,50,400)
    battleground = Battle()
    print("Name:{}, Attack:{}, Block:{}, Health:{}".format(l.name,l.attack, l.block, l.health))
    print()
    print("Name:{}, Attack:{}, Block:{}, Health:{}".format(s.name, s.attack, s.block, s.health))
    print()
    battleground.startfigth(l,s)
main()














