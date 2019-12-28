
import discord


def tagPlayer(player):
    return "<@{}>".format(player.id)

def displayPromotion(player, role):
    return tagPlayer(player) + " devient " + role + "\n"

def displayDestitution(role):
    return "Et perd son rôle " + role + "\n"

def displayDrink(role, nb):
    return role + " boit %d !\n" % nb
