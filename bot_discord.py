import os
import random
import discord
from discord.ext import commands

#initialisation
intents=discord.Intents.all()
intents.message_content = True
bot=commands.Bot(command_prefix="!", intents=intents)
#commands du bot

pileouface=("pile", "face")
@bot.command()
async def bonjour(ctx):
    await ctx.send(f"bonjour {ctx.author} !")
@bot.command()
async def salut(ctx):
    await ctx.send(f"salut {ctx.author} !")
    
@bot.command()
async def PileOuFace(ctx):
    a=random.choice(pileouface)
    await ctx.send(f"tu a eu {a} {ctx.author} !")

@bot.command()
async def pile_ou_face(ctx):
    a=random.choice(pileouface)
    await ctx.send(f"tu a eu {a} {ctx.author} !")
    
@bot.command()
async def comment_tu_vas(ctx):
    await ctx.send("je vas tres pas bien")

@bot.command()
async def ping_me(ctx):
    await ctx.send(f"@{ctx.author}")

@bot.command()
async def help_me(ctx):
    await ctx.send("``commande 1: bonjour/salut, te dit bonjour``")
    await ctx.send("``commande 2: PileOuFace, un simple pile ou face``")
    await ctx.send("``commande 3: comment_tu_vas, de dis si je vais bien(ps: c'est filenotfound qui me maltraite :/ )``")
#démarage
bot.run('MTI0ODkyMTM3MjkzMTkxNTgyNw.G55eik.f2E3zDz6mYelQ6fL0GiABBT4cUUQEc15zY80b4')