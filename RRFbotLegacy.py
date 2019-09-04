# Discord bot with discord.py test 1
# wrtten with the assistance of:
# https://boostlog.io/@junp1234/how-to-write-a-discord-bot-in-python-5a8e73aca7e5b7008ae1da8b
# by plscks
#
# Crafting component screenshots from Nexus Clash wiki
# http://wiki.nexuscla.sh/wiki/index.php?title=Crafting_Components
#
# Maybe this will work?
# Uses exclusively python 3.6
# Uses discord.py rewrite:
# python -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
# Good luck!!
#
#
#
########################
## STUFF TO IMPLEMENT ##
########################
#
# [] - Assign and remove  select roles based on commands
# [X] - SM timer that will ping Medic role
# [] - Setable raid reminder command
# [] - Creepier cat gif for Samus
#
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

@bot.command()
async def alch(ctx, *, potion='list'):
    potion = potion.lower()
    recipes = {}
    recipes.setdefault('acid affinity', []).append('Common: 1')
    recipes.setdefault('acid affinity', []).append('Uncommon: 3')
    recipes.setdefault('acid affinity', []).append('Rare: 1')
    recipes.setdefault('acid affinity', []).append('Fixed: Patch of Lichen')
    recipes.setdefault('cold affinity', []).append('Common: 3')
    recipes.setdefault('cold affinity', []).append('Uncommon: 1')
    recipes.setdefault('cold affinity', []).append('Rare: 1')
    recipes.setdefault('cold affinity', []).append('Fixed: Soul Ice')
    recipes.setdefault('combat clarity', []).append('Common: 2')
    recipes.setdefault('combat clarity', []).append('Uncommon: 1')
    recipes.setdefault('combat clarity', []).append('Rare: 2')
    recipes.setdefault('combat clarity', []).append('Fixed: Gold Ingot')
    recipes.setdefault('death affinity', []).append('Common: 3')
    recipes.setdefault('death affinity', []).append('Uncommon: 1')
    recipes.setdefault('death affinity', []).append('Rare: 1')
    recipes.setdefault('death affinity', []).append('Fixed: Sprig of Nightshade')
    recipes.setdefault('electrical affinity', []).append('Common: 2')
    recipes.setdefault('electrical affinity', []).append('Uncommon: 2')
    recipes.setdefault('electrical affinity', []).append('Rare: 1')
    recipes.setdefault('electrical affinity', []).append('Fixed: Spool of Copper Wire')
    recipes.setdefault('extended invisibility', []).append('Common: 1')
    recipes.setdefault('extended invisibility', []).append('Uncommon: 1')
    recipes.setdefault('extended invisibility', []).append('Rare: 3')
    recipes.setdefault('extended invisibility', []).append('Fixed: Small Bottle of Gunpowder')
    recipes.setdefault('fire affinity', []).append('Common: 2')
    recipes.setdefault('fire affinity', []).append('Uncommon: 3')
    recipes.setdefault('fire affinity', []).append('Rare: 0')
    recipes.setdefault('fire affinity', []).append('Fixed: Chunk of Brass')
    recipes.setdefault('flying', []).append('Common: 2')
    recipes.setdefault('flying', []).append('Uncommon: 1')
    recipes.setdefault('flying', []).append('Rare: 2')
    recipes.setdefault('flying', []).append('Fixed: Silver Ingot')
    recipes.setdefault('greater invulnerability', []).append('Common: 1')
    recipes.setdefault('greater invulnerability', []).append('Uncommon: 2')
    recipes.setdefault('greater invulnerability', []).append('Rare: 2')
    recipes.setdefault('greater invulnerability', []).append('Fixed: Chunk of Iron')
    recipes.setdefault('healing', []).append('Common: 2')
    recipes.setdefault('healing', []).append('Uncommon: 2')
    recipes.setdefault('healing', []).append('Rare: 1')
    recipes.setdefault('healing', []).append('Fixed: Skull')
    recipes.setdefault('holy affinity', []).append('Common: 1')
    recipes.setdefault('holy affinity', []).append('Uncommon: 3')
    recipes.setdefault('holy affinity', []).append('Rare: 1')
    recipes.setdefault('holy affinity', []).append('Fixed: Bunch of Paradise Lilies')
    recipes.setdefault('invisibility', []).append('Common: 1')
    recipes.setdefault('invisibility', []).append('Uncommon: 4')
    recipes.setdefault('invisibility', []).append('Rare: 0')
    recipes.setdefault('invisibility', []).append('Fixed: Batch of Mushrooms')
    recipes.setdefault('invulnerability', []).append('Common: 2')
    recipes.setdefault('invulnerability', []).append('Uncommon: 2')
    recipes.setdefault('invulnerability', []).append('Rare: 1')
    recipes.setdefault('invulnerability', []).append('Fixed: Lead Brick')
    recipes.setdefault('lesser invulnerability', []).append('Common: 3')
    recipes.setdefault('lesser invulnerability', []).append('Uncommon: 2')
    recipes.setdefault('lesser invulnerability', []).append('Rare: 0')
    recipes.setdefault('lesser invulnerability', []).append('Fixed: Batch of Leather')
    recipes.setdefault('magic recovery', []).append('Common: 1')
    recipes.setdefault('magic recovery', []).append('Uncommon: 1')
    recipes.setdefault('magic recovery', []).append('Rare: 3')
    recipes.setdefault('magic recovery', []).append('Fixed: Chunk of Onyx')
    recipes.setdefault('planar protection', []).append('Common: 3')
    recipes.setdefault('planar protection', []).append('Uncommon: 2')
    recipes.setdefault('planar protection', []).append('Rare: 0')
    recipes.setdefault('planar protection', []).append('Fixed: Handful of Grave Dirt')
    recipes.setdefault('regeneration', []).append('Common: 1')
    recipes.setdefault('regeneration', []).append('Uncommon: 2')
    recipes.setdefault('regeneration', []).append('Rare: 2')
    recipes.setdefault('regeneration', []).append('Fixed: Stygian Bone Leech')
    recipes.setdefault('strength', []).append('Common: 2')
    recipes.setdefault('strength', []).append('Uncommon: 1')
    recipes.setdefault('strength', []).append('Rare: 2')
    recipes.setdefault('strength', []).append('Fixed: Bag of Industrial Plastic')
    recipes.setdefault('unholy affinity', []).append('Common: 1')
    recipes.setdefault('unholy affinity', []).append('Uncommon: 3')
    recipes.setdefault('unholy affinity', []).append('Rare: 1')
    recipes.setdefault('unholy affinity', []).append('Fixed: Blood Ice')
    recipes.setdefault('water breathing', []).append('Common: 4')
    recipes.setdefault('water breathing', []).append('Uncommon: 1')
    recipes.setdefault('water breathing', []).append('Rare: 0')
    recipes.setdefault('water breathing', []).append('Fixed: Bunch of Lilies')
    if potion in recipes:
        final = '\n• '.join(recipes[potion])
        embed = discord.Embed(title=potion.title(), description=f'• {final}', color=0x00BFFF)
        await ctx.send(embed=embed)
    elif potion == 'list':
        fulllist = '\n• '.join(list(recipes.keys()))
        embed = discord.Embed(title='Usage:', description="'.alch <POTION_NAME>' to list ratio of components for potions\n (must be exact item name)", color=0x00BFFF)
        embed.add_field(name='Potions:', value=f'• {fulllist}')
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Potion **{potion}** not recognozed.')
    
@bot.command()
async def mats(ctx, *, comp='list'):
    comp = comp.lower()
    mats = {}
    materials = {}
    fixed = {}
    mats['bag of industrial plastic'] = 'https://imgur.com/RAUmHsu'
    mats['batch of leather'] = 'https://imgur.com/rEYpBUS'
    mats['batch of mushrooms'] = 'https://imgur.com/YniUM42'
    mats['blood ice'] = 'https://imgur.com/F2yL2AE'
    mats['bottle of holy water'] = 'https://imgur.com/uDHZMvW'
    mats['bottle of paradise water'] = 'https://imgur.com/YKK59Q1'
    mats['bunch of daisies'] = 'https://imgur.com/pF5T2YC'
    mats['bunch of lilies'] = 'https://imgur.com/i8EN96c'
    mats['bunch of paradise lilies'] = 'https://imgur.com/uzZbRXt'
    mats['chunk of brass'] = 'https://imgur.com/ROsCZE7'
    mats['chunk of iron'] = 'https://imgur.com/LYdUqjf'
    mats['chunk of ivory'] = 'https://imgur.com/NfzqBEA'
    mats['chunk of onyx'] = 'https://imgur.com/rVV3QN3'
    mats['chunk of steel'] = 'https://imgur.com/gRiHcpS'
    mats['chunk of stygian iron'] = 'https://imgur.com/aXYBg2F'
    mats['femur'] = 'https://imgur.com/yPlq4va'
    mats['gold ingot'] = 'https://imgur.com/KX87eRp'
    mats['handful of grave dirt'] = 'https://imgur.com/BdYz9K9'
    mats['healing herb'] = 'https://imgur.com/GxJn4ra'
    mats['humerus'] = 'https://imgur.com/IrMwt4K'
    mats['lead brick'] = 'https://imgur.com/apqTMpV'
    mats['patch of lichen'] = 'https://imgur.com/gNeP7wL'
    mats['patch of moss'] = 'https://imgur.com/ouqxOzc'
    mats['piece of stygian coal'] = 'https://imgur.com/wZBnZHI'
    mats['piece of wood'] = 'https://imgur.com/eTzHXuS'
    mats['rose'] = 'https://imgur.com/vUomB72'
    mats['silver ingot'] = 'https://imgur.com/09jzYcH'
    mats['skull'] = 'https://imgur.com/cLlw47F'
    mats['small bottle of gunpowder'] = 'https://imgur.com/Hszsnb6'
    mats['soul ice'] = 'https://imgur.com/iWCE2w0'
    mats['spool of copper wire'] = 'https://imgur.com/sDaBaFZ'
    mats['sprig of nightshade'] = 'https://imgur.com/ytXTMse'
    mats['stygian bone leech'] = 'https://imgur.com/A9ksCH5'
    fixed['patch of lichen'] = 'acid affinity'
    fixed['soul ice'] = 'cold affinity'
    fixed['gold ingot'] = 'combat clarity'
    fixed['sprig of nightshade'] = 'death affinity'
    fixed['spool of copper wire'] = 'electricity affinity'
    fixed['small bottle of gunpowder'] = 'extended invisibility'
    fixed['chunk of brass'] = 'fire affinity'
    fixed['silver ingot'] = 'flying'
    fixed['chunk of iron'] = 'greater invulnerability'
    fixed['skull'] = 'healing'
    fixed['bunch of paradise lilies'] = 'holy affinity'
    fixed['batch of mushrooms'] = 'invisibility'
    fixed['lead brick'] = 'invulnerability'
    fixed['batch of leather'] = 'lesser invulnerability'
    fixed['chunk of onyx'] = 'magic recovery'
    fixed['handful of grave dirt'] = 'planar protection'
    fixed['stygian bone leech'] = 'regeneration'
    fixed['bag of industrial plastic'] = 'strength'
    fixed['blood ice'] = 'unholy affinity'
    fixed['bunch of lilies'] = 'water breathing'
    materials['bag of industrial plastic'] = 'Rarity: Rare'
    materials['batch of leather'] = 'Rarity: Rare'
    materials['batch of mushrooms'] = 'Rarity: Uncommon'
    materials['blood ice'] = 'Rarity: Uncommon'
    materials['bottle of holy water'] = 'Rarity: Common'
    materials['bottle of paradise water'] = 'Rarity: Common'
    materials['bunch of daisies'] = 'Rarity: Uncommon'
    materials['bunch of lilies'] = 'Rarity: Rare'
    materials['bunch of paradise lilies'] = 'Rarity: Uncommon'
    materials['chunk of brass'] = 'Rarity: Uncommon'
    materials['chunk of iron'] = 'Rarity: Rare'
    materials['chunk of ivory'] = 'Rarity: Uncommon'
    materials['chunk of onyx'] = 'Rarity: Rare'
    materials['chunk of steel'] = 'Rarity: Common'
    materials['chunk of stygian iron'] = 'Rarity: Common'
    materials['femur'] = 'Rarity: Common'
    materials['gold ingot'] = 'Rarity: Uncommon'
    materials['handful of grave dirt'] = 'Rarity: Common'
    materials['healing herb'] = 'Rarity: Uncommon'
    materials['humerus'] = 'Rarity: Common'
    materials['lead brick'] = 'Rarity: Uncommon'
    materials['patch of lichen'] = 'Rarity: Uncommon'
    materials['patch of moss'] = 'Rarity: Uncommon'
    materials['piece of stygian coal'] = 'Rarity: Common'
    materials['piece of wood'] = 'Rarity: Common'
    materials['rose'] = 'Rarity: Common'
    materials['silver ingot'] = 'Rarity: Uncommon'
    materials['skull'] = 'Rarity: Common'
    materials['small bottle of gunpowder'] = 'Rarity: Rare'
    materials['soul ice'] = 'Rarity: Uncommon'
    materials['spool of copper wire'] = 'Rarity: Rare'
    materials['sprig of nightshade'] = 'Rarity: Rare'
    materials['stygian bone leech'] = 'Rarity: Common'
    if comp in mats:
        if comp in fixed:
            embed = discord.Embed(title=comp.title(), description=materials[comp] + '\nFixed ingredient in Potion of ' + fixed[comp].title(), color=0x00BFFF)
            embed.set_image(url=mats[comp] + '.png')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=comp.title(), description=materials[comp], color=0x00BFFF)
            embed.set_image(url=mats[comp] + '.png')
            await ctx.send(embed=embed)
    elif comp == 'list':
        fulllist = '\n• '.join(list(mats.keys()))
        embed = discord.Embed(title='Usage:', description="'.mats <MATERIAL_NAME>' - lists material rarity and search rates\n (must be exact item name)\nNote - Some images work very poorly, this is still a work in progress.\n\n'.mats common' - lists common materials\n'.mats uncommon' - lists uncommon materials\n'.mats rare' - lists rare materials", color=0x00BFFF)
        embed.add_field(name='Materials:', value='• ' + fulllist)
        await ctx.send(embed=embed)
    elif comp == 'common':
        common = [rarity for rarity,value in materials.items() if value == 'Rarity: Common']
        shortlist = '\n• '.join(common)
        embed = discord.Embed(title='Common Components:', description=f'• {shortlist}', color=0x00BFFF)
        await ctx.send(embed=embed)
    elif comp == 'uncommon':
        uncommon = [rarity for rarity,value in materials.items() if value == 'Rarity: Uncommon']
        shortlist = '\n• '.join(uncommon)
        embed = discord.Embed(title='Uncommon Components:', description=f'• {shortlist}', color=0x00BFFF)
        await ctx.send(embed=embed)
    elif comp == 'rare':
        rare = [rarity for rarity,value in materials.items() if value == 'Rarity: Rare']
        shortlist = '\n• '.join(rare)
        embed = discord.Embed(title='Rare Components:', description=f'• {shortlist}', color=0x00BFFF)
        await ctx.send(embed=embed)    
    else:
        await ctx.send(f'Item **{comp}** not recognozed.')
    
@bot.command()
async def craft(ctx, *, item='list'):
    item = item.lower()
    craft = {}
    craft.setdefault('carving knife', []).append('+4xp / +2AP')
    craft.setdefault('carving knife', []).append('1 Chunk of Steel')
    craft.setdefault('chainsaw', []).append('+14xp / +7AP')
    craft.setdefault('chainsaw', []).append('2 Chunk of Steel')
    craft.setdefault('chainsaw', []).append('1 Length of Chain')
    craft.setdefault('chainsaw', []).append('2 Bag of Industrial Plastic')
    craft.setdefault('cutlass', []).append('+10xp / +5AP')
    craft.setdefault('cutlass', []).append('2 Chunk of Steel')
    craft.setdefault('cutlass', []).append('1 Chunk of Brass')
    craft.setdefault('hatchet', []).append('+6xp / +3AP')
    craft.setdefault('hatchet', []).append('1 Chunk of Iron')
    craft.setdefault('hatchet', []).append('1 Piece of Wood')
    craft.setdefault('rapier', []).append('+10xp / +5AP')
    craft.setdefault('rapier', []).append('2 Chunk of Steel')
    craft.setdefault('rapier', []).append('1 Chunk of Iron')
    craft.setdefault('sabre', []).append('+10xp / +5AP')
    craft.setdefault('sabre', []).append('2 Chunk of Steel')
    craft.setdefault('sabre', []).append('1 Chunk of Iron')
    craft.setdefault('sword', []).append('+10xp / +5AP')
    craft.setdefault('sword', []).append('3 Chunk of Steel')
    craft.setdefault('tarnished sword', []).append('+10xp / +5AP')
    craft.setdefault('tarnished sword', []).append('2 Chunk of Steel')
    craft.setdefault('tarnished sword', []).append('1 Silver Ingot')
    craft.setdefault('torch', []).append('+8xp / +4AP')
    craft.setdefault('torch', []).append('1 Piece of Wood')
    craft.setdefault('torch', []).append('1 Batch of Leather')
    craft.setdefault('torch', []).append('1 Length of Rope')
    craft.setdefault('torch', []).append('1 Chunk of Brass')
    craft.setdefault('chainmail shirt', []).append('+20xp / +10AP')
    craft.setdefault('chainmail shirt', []).append('4 Chunk of Steel')
    craft.setdefault('fireman\'s jacket', []).append('+10xp / +5AP')
    craft.setdefault('fireman\'s jacket', []).append('2 Batch of Leather')
    craft.setdefault('fireman\'s jacket', []).append('1 Bag of Industrial Plastic')
    craft.setdefault('leather cuirass', []).append('+4xp / +2AP')
    craft.setdefault('leather cuirass', []).append('3 Batch of Leather')
    craft.setdefault('leather jacket', []).append('+4xp / +2AP')
    craft.setdefault('leather jacket', []).append('2 Batch of Leather')
    craft.setdefault('plate cuirass', []).append('+20xp / +10AP')
    craft.setdefault('plate cuirass', []).append('4 Chunk of Steel')
    craft.setdefault('plate cuirass', []).append('2 Batch of Leather')
    craft.setdefault('suit of light body armor', []).append('+20xp / +10AP')
    craft.setdefault('suit of light body armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of light body armor', []).append('3 Bag of Industrial Plastic')
    craft.setdefault('suit of military encounter armor', []).append('+30xp / +15AP')
    craft.setdefault('suit of military encounter armor', []).append('4 Bag of Industrial Plastic')
    craft.setdefault('suit of military encounter armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of police riot armor', []).append('+20xp / +10AP')
    craft.setdefault('suit of police riot armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of police riot armor', []).append('3 Bag of Industrial Plastic')
    craft.setdefault('flamethrower', []).append('+16 xp / +8AP')
    craft.setdefault('flamethrower', []).append('4 Chunk of Steel')
    craft.setdefault('flamethrower', []).append('1 Bag of Industrial Plastic')
    craft.setdefault('pistol', []).append('+8xp / +4AP')
    craft.setdefault('pistol', []).append('1 Chunk of Brass')
    craft.setdefault('pump action shotgun', []).append('+16xp / +8AP')
    craft.setdefault('pump action shotgun', []).append('3 Chunk of Steel')
    craft.setdefault('pump action shotgun', []).append('1 Chunk of Brass')
    craft.setdefault('pump action shotgun', []).append('1 Piece of Wood')
    craft.setdefault('rifle', []).append('+16xp / +8AP')
    craft.setdefault('rifle', []).append('5 Chunk of Steel')
    craft.setdefault('rifle', []).append('1 Chunk of Brass')
    craft.setdefault('rifle', []).append('1 Piece of Wood')
    craft.setdefault('sub-machine gun', []).append('+12xp / +6AP')
    craft.setdefault('sub-machine gun', []).append('2 Chunk of Steel')
    craft.setdefault('sub-machine gun', []).append('1 Chunk of Brass')
    craft.setdefault('long bow', []).append('+14xp / +7AP')
    craft.setdefault('long bow', []).append('3 Piece of Wood')
    craft.setdefault('short bow', []).append('+6xp / +3AP')
    craft.setdefault('short bow', []).append('1 Piece of Wood')
    craft.setdefault('sling', []).append('+8xp / +4AP')
    craft.setdefault('sling', []).append('2 Batch of Leather')
    craft.setdefault('compound bow', []).append('+10xp / +5AP')
    craft.setdefault('compound bow', []).append('2 Piece of Wood')
    craft.setdefault('compound bow', []).append('1 Bag of Industrial Plastic')
    if item in craft:
        final = '\n• '.join(craft[item])
        embed = discord.Embed(title=item.title(), description=final, color=0x00BFFF)
        await ctx.send(embed=embed)
    elif item == 'list':
        fulllist = '\n• '.join(list(craft.keys()))
        embed = discord.Embed(title='Usage:', description="'.craft <ITEM_NAME>' to list crafting XP and requirements\n (must be exact item name)", color=0x00BFFF)
        embed.add_field(name='Craftable Items:', value=f'• {fulllist}')
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Item **{item}** not recognozed as craftable')
        
@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)
    print(arg)

@bot.command()
async def sm(ctx, *, time='help'):
    author = ctx.message.author
    role =  discord.utils.get(ctx.guild.roles,id=541347064001331201)
    try:
        test = int(time) + 1
        if int(time) < 0:
            await ctx.send('Use a real, positive number of minutes please.')
            return
        elif int(time) > 90:
            await ctx.send('Use a real, positive number of minutes please.')
            return
        elif int(time) == 0:
             await ctx.send('That doesn\'t work yet!')
             return
        await ctx.send(f'Sorcerers Might alert set for {time} minutes!')
        time = (int(time) * 60) - 60
        await asyncio.sleep(time)
        if author.nick == None:
            sep = '#'
            nick = str(author)
            nick = nick.split(sep, 1)[0]
            await ctx.send(f'{role.mention}: {nick} is off of Sorcerers Might in about 1 minute!')
        else:
            await ctx.send(f'{role.mention}: {author.nick} is off of Sorcerers Might in about 1 minute!')
    except ValueError:
        embed = discord.Embed(title='Usage:', description="'.sm <TIME IN MINUTES>' to set a timer for SM to ping once up", color=0x00BFFF)
        await ctx.send(embed=embed)

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='545312880162111513')
    await ctx.send('doing stuff out of while not')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await ctx.send('doing stuff in while not?')
        await asyncio.sleep(60) # task runs every 60 seconds

@bot.command()
async def bgtask(ctx):
    client.loop.create_task(my_background_task())
        
@bot.command()
async def greet(ctx):
    await ctx.send(":thonk: Why hello, there! <:kitty:491077122434138124>")

@bot.command()
async def cat(ctx):
    await ctx.send("http://www.animalslook.com/media/loki-is-one-scary-cat-10-pictures/loki-is-one-scary-cat-10-pictures-1.jpg")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="RRFBot", description="A work in progress. Gives different useful info about Nexus Clash", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="plscks")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__**Nexus Clash RRFBot**__", description="*An ever evolving Nexus Clash RRFBot. List of commands are:*", color=0xeee657)

    #embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    #embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False1)
    embed.add_field(name=".sm", value="Sets a timer for Sorcerers Might, and alerts Medic role when about up.", inline=False)
    embed.add_field(name=".craft", value="Gives crafting info of items.", inline=False)
    embed.add_field(name=".mats", value="Gives materials search rates and rarity.", inline=False)
    embed.add_field(name=".alch", value="Gives potion recipe ratios.", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".cat", value="Gives a cute fORB gif to lighten up the mood???", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the RRFBot.", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)
    await ctx.send(embed=embed)

if __name__ == '__main__':
    token = parse()
    bot.run(token)
