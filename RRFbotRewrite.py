# RRFbot version 2.0 - rewrite for python 3.7+
# written by plscks
#
# Utilizes discord.py
#
# Is this a test?
# It has to be.
# Right?
# Rewrite.
# Go!
import argparse
import asyncio
import discord
from discord import Guild
from discord import Role
from discord.ext import commands

bot = commands.Bot(command_prefix='.', desciption='A bot that does bot stuff maybe?')
client = discord.Client()

def parse():
    # I don't know what I'm doing...
    parser = argparse.ArgumentParser('Discord Bot Test1')
    parser.add_argument('-t', '--token', help='Your bots token', action='store', dest='token')
    args = parser.parse_args()
    token = args.token
    return token
    # Now I kinda know what I'm doing???

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------')
    print('Doing RRFBot stuff')
