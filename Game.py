
import discord
import random
import State
from State import STATE
from Utils import *

class Game:

    def __init__(self):
        self.playerList = []
        self.indexCurrentPlayer = -1

        self.idDragon = -1
        self.idGod = -1
        self.idPrincess = -1
        self.idHero = -1
        self.idSquire = -1
        self.idClochard = -1
        self.idCatin = -1
        self.idDemon = -1
        self.idOracle = -1
        self.idTavernier = -1
        self.idPrisoonier = -1

        self.state = STATE.INIT
        self.de1 = -1
        self.de2 = -1
        self.de3 = -1
        self.oldDe1 = -1
        self.oldDe2 = -1
        self.oldDe3 = -1

    def addPlayer(self, player):
        if (player in self.playerList):
            return "Ce joueur est déjà dans la partie."
        self.playerList.append(player)
        return "{} a rejoind la partie !".format(player.name)

    def removePlayer(self, player):
        if not (player in self.playerList):
            return

        self.playerList.remove(player)
        idPlayer = player.id

        if (self.idDragon == idPlayer): self.idDragon = -1
        if (self.idGod == idPlayer): self.idGod = -1
        if (self.idPrincess == idPlayer): self.idPrincess = -1
        if (self.idHero == idPlayer): self.idHero = -1
        if (self.idSquire == idPlayer): self.idSquire = -1
        if (self.idClochard == idPlayer): self.idClochard = -1
        if (self.idCatin == idPlayer): self.idCatin = -1
        if (self.idDemon == idPlayer): self.idDemon = -1
        if (self.idOracle == idPlayer): self.idOracle = -1
        if (self.idTavernier == idPlayer): self.idTavernier = -1
        if (self.idPrisoonier == idPlayer): self.idPrisoonier = -1
        return "{} a quitté la partie !".format(player.name)

    def nextTurn(self):
        indexCurrentPlayer = (self.indexCurrentPlayer+1)%len(self.playerList)

        player = self.playerList[self.indexCurrentPlayer]
        out = "Tour de " + tagPlayer(player)

        return out

    def checkState(self):
        if (self.state == STATE.CATIN_DEFEND and self.idCatin == -1):
            self.state = STATE.HERO_DEFEND
            return "Il n'y a pas de catin !\n"

        elif (self.state == STATE.HERO_DEFEND and self.idHero == -1):
            self.state = STATE.GOD_ATTACK
            return "Il n'y a pas de héro !\n"
        return ""


    def someoneDrink(self, idPlayer, nb):
        res = ""
        if idPlayer == self.idHero:
            res += displayDrink("ecuyer", nb)
        if idPlayer == self.idPrincess:
            res += displayDrink("hero", nb)
        if idPlayer == self.idDragon:
            res += "Dragon soufle ! TODO\n"

        return res


    def begin(self):
        if (len(self.playerList) == 0):
            return "Pas encore de joueurs dans la partie !"

        if (self.state == STATE.INIT):
            self.state = STATE.ROLLING
            out = "La partie commence ! "
            out += self.nextTurn()
            return out

    def roll(self, player):
        if (player.id != self.playerList[self.indexCurrentPlayer].id):
            return "Ce n'est pas à toi de jouer, tu bois !"

        # if bonne personne de lancer les des
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        self.de3 = random.randint(1, 6)

        lancer = str(de1) + " " + str(de2) + " " + str(self.de3) + "\n"

        self.de1 = max(de1, de2)
        self.de2 = min(de1, de2)
        return lancer


    def solve(self):
        de1 = self.de1
        de2 = self.de2
        de3 = self.de3

        if ((de1 == de2) and (de1 <= 3)):
            if (de1 == 1 and de3 == 1):
                return self.clochard()
            else:
                return self.hero()

        if ((de1 == de2) and (de1 >= 4)):
            if (de1 == 6):
                if (de3 == 6):
                    res = "Dieu-Démon !\n"
                else:
                    res = "Dieu Incontesté !\n"
            else:
                res = "Dieu !\n"
        if (de1 + de2 == 7):
            res = "Dieu attaque le village !\n"
            return self.godAttack()

        if (de1 == 6):
            res = "Distribue %d !\n" % de3

        if (de1 == 2 and de2 == 1):
            return self.oracle()
        if (de1 == 3 and de2 == 1):
            res = "Ecuyer !\n"
        if (de1 == 4 and de2 == 1):
            res = "Catin !\n"
        if (de1 == 5 and de2 == 1):
            return self.everyoneDrink(de3)

        if (de1 == 3 and de2 == 2):
            return self.goPrison(de3)
        if (de1 == 4 and de2 == 2):
            return self.everyoneDrink(de3)
        if (de1 == 5 and de2 == 3):
            return self.tavernier()
        if (de1 == 5 and de2 == 4):
            return self.princesse()

        return res + "TODO\n"

    def clochard(self):
        self.idClochard = self.indexCurrentPlayer
        return displayPromotion(self.playerList[self.indexCurrentPlayer], "clochard")

    def hero(self):
        self.idHero = self.indexCurrentPlayer
        if self.idGod == self.idHero:
            out = tagPlayer(self.playerList[self.indexCurrentPlayer]) + " est déjà Dieu !\n"
        else:
            out = displayPromotion(self.playerList[self.indexCurrentPlayer], "héro")
            if self.idSquire == self.idHero:
                self.idSquire = -1
                out += displayDestitution("d'écuyer")
        return out

    def goPrison(self, de3):
        if self.idPrisoonier != -1:
            return "Il y a déjà quelqu'un en prison !\n"

        self.idPrisoonier = self.indexCurrentPlayer
        return tagPlayer(self.playerList[self.indexCurrentPlayer]) + " va en prison, et boit %d pour fêter ça !\n" % de3


    def princesse(self):
        self.idPrincess == self.indexCurrentPlayer
        return displayPromotion(self.playerList[self.indexCurrentPlayer], "princesse")

    def oracle(self):
        self.idOracle = self.indexCurrentPlayer
        return displayPromotion(self.playerList[self.indexCurrentPlayer], "oracle")

    def tavernier(self):
        self.idTavernier == self.indexCurrentPlayer
        return displayPromotion(self.playerList[self.indexCurrentPlayer], "tavernier")

    def everyoneDrink(self, de):
        return "Tous le monde boit %d !" % de

    def godAttack(self):
        res = "Dieu attaque le village ! "
        res += "On joue pour %d.\n" % self.de1
        if (self.idGod == -1):
            return res + "Il n'y a pas encore de Dieu !\n"

        res += "La catin défend le village !\n"
        self.state = STATE.CATIN_DEFEND
        check = self.checkState()
        if (check != ""):
            res += check
            res += "Le héro défend le village !\n"
            res += self.checkState()
        return res

    def defend(self, player):
        de = random.randint(1, 6)
        res  = str(de) + "\n"
        if (self.state == STATE.CATIN_DEFEND and player.id == self.idCatin):
            return self.catinDefend(de)
        elif (self.state == STATE.HERO_DEFEND and player.id == self.idHero):
            return self.heroDefend(de)
        else:
            return tagPlayer(player) + " tu bois !\n"

    def catinDefend(self, de):
        if (de < 6):
            res = "La catin boit %d !\n" % de
            self.state = STATE.HERO_DEFEND
            res += "Le héro défend le village !\n"
            res += self.checkState()
        else:
            res = "Le Dieu est vaincu !\n"
            self.state = STATE.ROLLING

        return res

    def heroDefend(self, de):
        res = ""
        if de == 1:
            res = "Cul Sec !\n"
            res += "(Nan sérieux c'est une règle de merde t'es pas obligé...)\n"
        elif de == 6:
            res = "Dieu boit %d !\n" % self.de1
        else:
            if de <= 3:
                res = "Le héro boit %d !\n" % self.de1
            res += "Dieu distribue %d !\n" % self.de1

        return res

