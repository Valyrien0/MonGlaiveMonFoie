# bot.py
#https://gist.github.com/BrandonCravener/8aea1f908ccfa31fc99d3d03d02ed8d://gist.github.com/BrandonCravener/8aea1f908ccfa31fc99d3d03d02ed8d8


# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be

# https://www.reddit.com/r/discordapp/comments/bzg2pp/attributeerror_client_object_has_no_attribute_add/


import os

import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

from Game import Game
from State import STATE

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

bot.permissions = 8
game = Game()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print("v2")

@bot.command(name='join')
async def join(ctx, ):
    newPlayer = ctx.message.author
    out = game.addPlayer(newPlayer)
    await ctx.send(out)

@bot.command(name='leave')
async def leave(ctx):
    oldPlayer = ctx.message.author
    out = game.removePlayer(oldPlayer)
    await ctx.send(out)

@bot.command(pass_context=True)
async def begin(ctx):
    out = game.begin()
    await ctx.send(out)

@bot.command(name='roll')
async def roll(ctx):
    out = game.roll(ctx.message.author)
    await ctx.send(out)
    await ctx.send("TODO : Check clochard, prisonnier, démon, duel de paysan")

    out = game.solve()
    await ctx.send(out)

    if game.state == STATE.ROLLING:
        await ctx.send(game.nextTurn())

@bot.command(name='defend')
async def defend(ctx):
    out = game.defend(ctx.message.author)
    await ctx.send(out)

@bot.command(name='give')
async def give(ctx):
    # Doit recevoir joueur et nombre de gorgées
    await ctx.send("TODO\n")


@bot.command(name='blow')
async def blow(ctx):
    # Doit recevoir une direction ?
    await ctx.send("TODO\n")

@bot.command(pass_context=True)
# @commands.has_role("Admin")
async def roles(ctx):
    member = ctx.message.author
    test = discord.utils.get(member.guild.roles, name="test")
    await member.add_roles(test)

bot.run(token)
