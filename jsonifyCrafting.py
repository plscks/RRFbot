# output crafting lists as json for use in RRFBot
import json

def alch():
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
    return recipes

def craft():
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
    return craft

def masterList():
    masterList = {}
    masterList.setdefault('carving knife', []).append('+4xp / +2AP')
    masterList.setdefault('carving knife', []).append('1 Chunk of Steel')
    masterList.setdefault('chainsaw', []).append('+14xp / +7AP')
    masterList.setdefault('chainsaw', []).append('2 Chunk of Steel')
    masterList.setdefault('chainsaw', []).append('1 Length of Chain')
    masterList.setdefault('chainsaw', []).append('2 Bag of Industrial Plastic')
    masterList.setdefault('cutlass', []).append('+10xp / +5AP')
    masterList.setdefault('cutlass', []).append('2 Chunk of Steel')
    masterList.setdefault('cutlass', []).append('1 Chunk of Brass')
    masterList.setdefault('hatchet', []).append('+6xp / +3AP')
    masterList.setdefault('hatchet', []).append('1 Chunk of Iron')
    masterList.setdefault('hatchet', []).append('1 Piece of Wood')
    masterList.setdefault('rapier', []).append('+10xp / +5AP')
    masterList.setdefault('rapier', []).append('2 Chunk of Steel')
    masterList.setdefault('rapier', []).append('1 Chunk of Iron')
    masterList.setdefault('sabre', []).append('+10xp / +5AP')
    masterList.setdefault('sabre', []).append('2 Chunk of Steel')
    masterList.setdefault('sabre', []).append('1 Chunk of Iron')
    masterList.setdefault('sword', []).append('+10xp / +5AP')
    masterList.setdefault('sword', []).append('3 Chunk of Steel')
    masterList.setdefault('tarnished sword', []).append('+10xp / +5AP')
    masterList.setdefault('tarnished sword', []).append('2 Chunk of Steel')
    masterList.setdefault('tarnished sword', []).append('1 Silver Ingot')
    masterList.setdefault('torch', []).append('+8xp / +4AP')
    masterList.setdefault('torch', []).append('1 Piece of Wood')
    masterList.setdefault('torch', []).append('1 Batch of Leather')
    masterList.setdefault('torch', []).append('1 Length of Rope')
    masterList.setdefault('torch', []).append('1 Chunk of Brass')
    masterList.setdefault('chainmail shirt', []).append('+20xp / +10AP')
    masterList.setdefault('chainmail shirt', []).append('4 Chunk of Steel')
    masterList.setdefault('fireman\'s jacket', []).append('+10xp / +5AP')
    masterList.setdefault('fireman\'s jacket', []).append('2 Batch of Leather')
    masterList.setdefault('fireman\'s jacket', []).append('1 Bag of Industrial Plastic')
    masterList.setdefault('leather cuirass', []).append('+4xp / +2AP')
    masterList.setdefault('leather cuirass', []).append('3 Batch of Leather')
    masterList.setdefault('leather jacket', []).append('+4xp / +2AP')
    masterList.setdefault('leather jacket', []).append('2 Batch of Leather')
    masterList.setdefault('plate cuirass', []).append('+20xp / +10AP')
    masterList.setdefault('plate cuirass', []).append('4 Chunk of Steel')
    masterList.setdefault('plate cuirass', []).append('2 Batch of Leather')
    masterList.setdefault('suit of light body armor', []).append('+20xp / +10AP')
    masterList.setdefault('suit of light body armor', []).append('2 Batch of Leather')
    masterList.setdefault('suit of light body armor', []).append('3 Bag of Industrial Plastic')
    masterList.setdefault('suit of military encounter armor', []).append('+30xp / +15AP')
    masterList.setdefault('suit of military encounter armor', []).append('4 Bag of Industrial Plastic')
    masterList.setdefault('suit of military encounter armor', []).append('2 Batch of Leather')
    masterList.setdefault('suit of police riot armor', []).append('+20xp / +10AP')
    masterList.setdefault('suit of police riot armor', []).append('2 Batch of Leather')
    masterList.setdefault('suit of police riot armor', []).append('3 Bag of Industrial Plastic')
    masterList.setdefault('flamethrower', []).append('+16 xp / +8AP')
    masterList.setdefault('flamethrower', []).append('4 Chunk of Steel')
    masterList.setdefault('flamethrower', []).append('1 Bag of Industrial Plastic')
    masterList.setdefault('pistol', []).append('+8xp / +4AP')
    masterList.setdefault('pistol', []).append('1 Chunk of Brass')
    masterList.setdefault('pump action shotgun', []).append('+16xp / +8AP')
    masterList.setdefault('pump action shotgun', []).append('3 Chunk of Steel')
    masterList.setdefault('pump action shotgun', []).append('1 Chunk of Brass')
    masterList.setdefault('pump action shotgun', []).append('1 Piece of Wood')
    masterList.setdefault('rifle', []).append('+16xp / +8AP')
    masterList.setdefault('rifle', []).append('5 Chunk of Steel')
    masterList.setdefault('rifle', []).append('1 Chunk of Brass')
    masterList.setdefault('rifle', []).append('1 Piece of Wood')
    masterList.setdefault('sub-machine gun', []).append('+12xp / +6AP')
    masterList.setdefault('sub-machine gun', []).append('2 Chunk of Steel')
    masterList.setdefault('sub-machine gun', []).append('1 Chunk of Brass')
    masterList.setdefault('long bow', []).append('+14xp / +7AP')
    masterList.setdefault('long bow', []).append('3 Piece of Wood')
    masterList.setdefault('short bow', []).append('+6xp / +3AP')
    masterList.setdefault('short bow', []).append('1 Piece of Wood')
    masterList.setdefault('sling', []).append('+8xp / +4AP')
    masterList.setdefault('sling', []).append('2 Batch of Leather')
    masterList.setdefault('compound bow', []).append('+10xp / +5AP')
    masterList.setdefault('compound bow', []).append('2 Piece of Wood')
    masterList.setdefault('compound bow', []).append('1 Bag of Industrial Plastic')
    masterList.setdefault('acid affinity', []).append('Common: 1')
    masterList.setdefault('acid affinity', []).append('Uncommon: 3')
    masterList.setdefault('acid affinity', []).append('Rare: 1')
    masterList.setdefault('acid affinity', []).append('Fixed: Patch of Lichen')
    masterList.setdefault('cold affinity', []).append('Common: 3')
    masterList.setdefault('cold affinity', []).append('Uncommon: 1')
    masterList.setdefault('cold affinity', []).append('Rare: 1')
    masterList.setdefault('cold affinity', []).append('Fixed: Soul Ice')
    masterList.setdefault('combat clarity', []).append('Common: 2')
    masterList.setdefault('combat clarity', []).append('Uncommon: 1')
    masterList.setdefault('combat clarity', []).append('Rare: 2')
    masterList.setdefault('combat clarity', []).append('Fixed: Gold Ingot')
    masterList.setdefault('death affinity', []).append('Common: 3')
    masterList.setdefault('death affinity', []).append('Uncommon: 1')
    masterList.setdefault('death affinity', []).append('Rare: 1')
    masterList.setdefault('death affinity', []).append('Fixed: Sprig of Nightshade')
    masterList.setdefault('electrical affinity', []).append('Common: 2')
    masterList.setdefault('electrical affinity', []).append('Uncommon: 2')
    masterList.setdefault('electrical affinity', []).append('Rare: 1')
    masterList.setdefault('electrical affinity', []).append('Fixed: Spool of Copper Wire')
    masterList.setdefault('extended invisibility', []).append('Common: 1')
    masterList.setdefault('extended invisibility', []).append('Uncommon: 1')
    masterList.setdefault('extended invisibility', []).append('Rare: 3')
    masterList.setdefault('extended invisibility', []).append('Fixed: Small Bottle of Gunpowder')
    masterList.setdefault('fire affinity', []).append('Common: 2')
    masterList.setdefault('fire affinity', []).append('Uncommon: 3')
    masterList.setdefault('fire affinity', []).append('Rare: 0')
    masterList.setdefault('fire affinity', []).append('Fixed: Chunk of Brass')
    masterList.setdefault('flying', []).append('Common: 2')
    masterList.setdefault('flying', []).append('Uncommon: 1')
    masterList.setdefault('flying', []).append('Rare: 2')
    masterList.setdefault('flying', []).append('Fixed: Silver Ingot')
    masterList.setdefault('greater invulnerability', []).append('Common: 1')
    masterList.setdefault('greater invulnerability', []).append('Uncommon: 2')
    masterList.setdefault('greater invulnerability', []).append('Rare: 2')
    masterList.setdefault('greater invulnerability', []).append('Fixed: Chunk of Iron')
    masterList.setdefault('healing', []).append('Common: 2')
    masterList.setdefault('healing', []).append('Uncommon: 2')
    masterList.setdefault('healing', []).append('Rare: 1')
    masterList.setdefault('healing', []).append('Fixed: Skull')
    masterList.setdefault('holy affinity', []).append('Common: 1')
    masterList.setdefault('holy affinity', []).append('Uncommon: 3')
    masterList.setdefault('holy affinity', []).append('Rare: 1')
    masterList.setdefault('holy affinity', []).append('Fixed: Bunch of Paradise Lilies')
    masterList.setdefault('invisibility', []).append('Common: 1')
    masterList.setdefault('invisibility', []).append('Uncommon: 4')
    masterList.setdefault('invisibility', []).append('Rare: 0')
    masterList.setdefault('invisibility', []).append('Fixed: Batch of Mushrooms')
    masterList.setdefault('invulnerability', []).append('Common: 2')
    masterList.setdefault('invulnerability', []).append('Uncommon: 2')
    masterList.setdefault('invulnerability', []).append('Rare: 1')
    masterList.setdefault('invulnerability', []).append('Fixed: Lead Brick')
    masterList.setdefault('lesser invulnerability', []).append('Common: 3')
    masterList.setdefault('lesser invulnerability', []).append('Uncommon: 2')
    masterList.setdefault('lesser invulnerability', []).append('Rare: 0')
    masterList.setdefault('lesser invulnerability', []).append('Fixed: Batch of Leather')
    masterList.setdefault('magic recovery', []).append('Common: 1')
    masterList.setdefault('magic recovery', []).append('Uncommon: 1')
    masterList.setdefault('magic recovery', []).append('Rare: 3')
    masterList.setdefault('magic recovery', []).append('Fixed: Chunk of Onyx')
    masterList.setdefault('planar protection', []).append('Common: 3')
    masterList.setdefault('planar protection', []).append('Uncommon: 2')
    masterList.setdefault('planar protection', []).append('Rare: 0')
    masterList.setdefault('planar protection', []).append('Fixed: Handful of Grave Dirt')
    masterList.setdefault('regeneration', []).append('Common: 1')
    masterList.setdefault('regeneration', []).append('Uncommon: 2')
    masterList.setdefault('regeneration', []).append('Rare: 2')
    masterList.setdefault('regeneration', []).append('Fixed: Stygian Bone Leech')
    masterList.setdefault('strength', []).append('Common: 2')
    masterList.setdefault('strength', []).append('Uncommon: 1')
    masterList.setdefault('strength', []).append('Rare: 2')
    masterList.setdefault('strength', []).append('Fixed: Bag of Industrial Plastic')
    masterList.setdefault('unholy affinity', []).append('Common: 1')
    masterList.setdefault('unholy affinity', []).append('Uncommon: 3')
    masterList.setdefault('unholy affinity', []).append('Rare: 1')
    masterList.setdefault('unholy affinity', []).append('Fixed: Blood Ice')
    masterList.setdefault('water breathing', []).append('Common: 4')
    masterList.setdefault('water breathing', []).append('Uncommon: 1')
    masterList.setdefault('water breathing', []).append('Rare: 0')
    masterList.setdefault('water breathing', []).append('Fixed: Bunch of Lilies')
    masterList['bag of industrial plastic'] = 'Rarity: Rare'
    masterList['batch of leather'] = 'Rarity: Rare'
    masterList['batch of mushrooms'] = 'Rarity: Uncommon'
    masterList['blood ice'] = 'Rarity: Uncommon'
    masterList['bottle of holy water'] = 'Rarity: Common'
    masterList['bottle of paradise water'] = 'Rarity: Common'
    masterList['bunch of daisies'] = 'Rarity: Uncommon'
    masterList['bunch of lilies'] = 'Rarity: Rare'
    masterList['bunch of paradise lilies'] = 'Rarity: Uncommon'
    masterList['chunk of brass'] = 'Rarity: Uncommon'
    masterList['chunk of iron'] = 'Rarity: Rare'
    masterList['chunk of ivory'] = 'Rarity: Uncommon'
    masterList['chunk of onyx'] = 'Rarity: Rare'
    masterList['chunk of steel'] = 'Rarity: Common'
    masterList['chunk of stygian iron'] = 'Rarity: Common'
    masterList['femur'] = 'Rarity: Common'
    masterList['gold ingot'] = 'Rarity: Uncommon'
    masterList['handful of grave dirt'] = 'Rarity: Common'
    masterList['healing herb'] = 'Rarity: Uncommon'
    masterList['humerus'] = 'Rarity: Common'
    masterList['lead brick'] = 'Rarity: Uncommon'
    masterList['patch of lichen'] = 'Rarity: Uncommon'
    masterList['patch of moss'] = 'Rarity: Uncommon'
    masterList['piece of stygian coal'] = 'Rarity: Common'
    masterList['piece of wood'] = 'Rarity: Common'
    masterList['rose'] = 'Rarity: Common'
    masterList['silver ingot'] = 'Rarity: Uncommon'
    masterList['skull'] = 'Rarity: Common'
    masterList['small bottle of gunpowder'] = 'Rarity: Rare'
    masterList['soul ice'] = 'Rarity: Uncommon'
    masterList['spool of copper wire'] = 'Rarity: Rare'
    masterList['sprig of nightshade'] = 'Rarity: Rare'
    masterList['stygian bone leech'] = 'Rarity: Common'
    return masterList

def masterOutput(type):
    masterList = {}
    if type == 'craft':
        masterCraftList = craft()
        return masterCraftList
    elif type == 'ratio':
        masterRatio = alch()
        return masterRatio
    #masterList = {}

    #for k, v in masterLocations.items():
    #    locationData[k] = getItemRates(k, v)
    #    for key, value in locationData[k].items():
    #        if key in masterList:
    #            masterList[key].update(value)
    #        else:
    #            masterList[key] = value
    #return masterList

if __name__ == "__main__":
    #craftList = masterOutput('craft')
    #ratioList = masterOutput('ratio')
    #print('Making alchemy ratio json...')
    #with open('ratioList.json', 'w') as json_file:
    #    json.dump(ratioList, json_file)
    #print('Making crafting recipe json...')
    #with open('craftList.json', 'w') as json_file:
    #    json.dump(craftList, json_file)
    print('Making master json...')
    with open('masterList.json', 'w') as json_file:
        json.dump(masterList(), json_file)
