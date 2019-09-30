// A simple test of array database
// Ugh.
var masterListArray = initMasterArray();
var pants = ['shirt', 'buttons', 'zipper'];
console.log(masterListArray);

doStuff();

function doStuff() {
  console.log('Doing stuff inside of a function:\n');
  console.log(masterListArray);
  console.log(typeof(masterListArray));
  console.log('Did stuff in the function.');
}

////////////////////////////////////
// ADD ALL CRAFTING DATA TO ARRAY //
////////////////////////////////////
function initMasterArray() {
  var masterList = [];
  masterList['craft'] = [];
  masterList['alch'] = [];
  masterList['components'] = [];
  masterList['craft']['carving knife'] = ['+4xp / +2AP', '1 Chunk of Steel'];
  masterList['craft']['chainsaw'] = ['+14xp / +7AP', '2 Chunk of Steel', '1 Length of Chain', '2 Bag of Industrial Plastic'];
  masterList['craft']['cutlass'] = ['+10xp / +5AP', '2 Chunk of Steel', '1 Chunk of Brass'];
  masterList['craft']['hatchet'] = ['+6xp / +3AP', '1 Chunk of Iron', '1 Piece of Wood'];
  masterList['craft']['rapier'] = ['+10xp / +5AP', '2 Chunk of Steel', '1 Chunk of Iron'];
  masterList['craft']['sabre'] = ['+10xp / +5AP', '2 Chunk of Steel', '1 Chunk of Iron'];
  masterList['craft']['sword'] = ['+10xp / +5AP', '3 Chunk of Steel'];
  masterList['craft']['tarnished sword'] = ['+10xp / +5AP', '2 Chunk of Steel', '1 Silver Ingot'];
  masterList['craft']['torch'] = ['+8xp / +4AP', '1 Piece of Wood', '1 Batch of Leather', '1 Length of Rope', '1 Chunk of Brass'];
  masterList['craft']['chainmail shirt'] = ['+20xp / +10AP', '4 Chunk of Steel'];
  masterList['craft']['fireman\'s jacket'] = ['+10xp / +5AP', '2 Batch of Leather', '1 Bag of Industrial Plastic'];
  masterList['craft']['leather cuirass'] = ['+4xp / +2AP', '3 Batch of Leather'];
  masterList['craft']['leather jacket'] = ['+4xp / +2AP', '2 Batch of Leather'];
  masterList['craft']['plate cuirass'] = ['+20xp / +10AP', '4 Chunk of Steel', '2 Batch of Leather'];
  masterList['craft']['suit of light body armor'] = ['+20xp / +10AP', '2 Batch of Leather', '3 Bag of Industrial Plastic'];
  masterList['craft']['suit of military encounter armor'] = ['+30xp / +15AP', '4 Bag of Industrial Plastic', '2 Batch of Leather'];
  masterList['craft']['suit of police riot armor'] = ['+20xp / +10AP', '2 Batch of Leather', '3 Bag of Industrial Plastic'];
  masterList['craft']['flamethrower'] = ['+16 xp / +8AP', '4 Chunk of Steel', '1 Bag of Industrial Plastic'];
  masterList['craft']['pistol'] = ['+8xp / +4AP', '1 Chunk of Brass'];
  masterList['craft']['pump action shotgun'] = ['+16xp / +8AP', '3 Chunk of Steel', '1 Chunk of Brass', '1 Piece of Wood'];
  masterList['craft']['rifle'] = ['+16xp / +8AP', '5 Chunk of Steel', '1 Chunk of Brass', '1 Piece of Wood'];
  masterList['craft']['sub-machine gun'] = ['+12xp / +6AP', '2 Chunk of Steel', '1 Chunk of Brass'];
  masterList['craft']['long bow'] = ['+14xp / +7AP', '3 Piece of Wood'];
  masterList['craft']['short bow'] = ['+6xp / +3AP', '1 Piece of Wood'];
  masterList['craft']['sling'] = ['+8xp / +4AP', '2 Batch of Leather'];
  masterList['craft']['compound bow'] = ['+10xp / +5AP', '2 Piece of Wood', '1 Bag of Industrial Plastic'];
  masterList['alch']['acid affinity'] = ['Common: 1', 'Uncommon: 3', 'Rare: 1', 'Fixed: Patch of Lichen'];
  masterList['alch']['cold affinity'] = ['Common: 3', 'Uncommon: 1', 'Rare: 1', 'Fixed: Soul Ice'];
  masterList['alch']['combat clarity'] = ['Common: 2', 'Uncommon: 1', 'Rare: 2', 'Fixed: Gold Ingot'];
  masterList['alch']['death affinity'] = ['Common: 3', 'Uncommon: 1', 'Rare: 1', 'Fixed: Sprig of Nightshade'];
  masterList['alch']['electrical affinity'] = ['Common: 2', 'Uncommon: 2', 'Rare: 1', 'Fixed: Spool of Copper Wire'];
  masterList['alch']['extended invisibility'] = ['Common: 1', 'Uncommon: 1', 'Rare: 3', 'Fixed: Small Bottle of Gunpowder'];
  masterList['alch']['fire affinity'] = ['Common: 2', 'Uncommon: 3', 'Rare: 0', 'Fixed: Chunk of Brass'];
  masterList['alch']['flying'] = ['Common: 2', 'Uncommon: 1', 'Rare: 2', 'Fixed: Silver Ingot'];
  masterList['alch']['greater invulnerability'] = ['Common: 1', 'Uncommon: 2', 'Rare: 2', 'Fixed: Chunk of Iron'];
  masterList['alch']['healing'] = ['Common: 2', 'Uncommon: 2', 'Rare: 1', 'Fixed: Skull'];
  masterList['alch']['holy affinity'] = ['Common: 1', 'Uncommon: 3', 'Rare: 1', 'Fixed: Bunch of Paradise Lilies'];
  masterList['alch']['invisibility'] = ['Common: 1', 'Uncommon: 4', 'Rare: 0', 'Fixed: Batch of Mushrooms'];
  masterList['alch']['invulnerability'] = ['Common: 2', 'Uncommon: 2', 'Rare: 1', 'Fixed: Lead Brick'];
  masterList['alch']['lesser invulnerability'] = ['Common: 3', 'Uncommon: 2', 'Rare: 0', 'Fixed: Batch of Leather'];
  masterList['alch']['magic recovery'] = ['Common: 1', 'Uncommon: 1', 'Rare: 3', 'Fixed: Chunk of Onyx'];
  masterList['alch']['planar protection'] = ['Common: 3', 'Uncommon: 2', 'Rare: 0', 'Fixed: Handful of Grave Dirt'];
  masterList['alch']['regeneration'] = ['Common: 1', 'Uncommon: 2', 'Rare: 2', 'Fixed: Stygian Bone Leech'];
  masterList['alch']['strength'] = ['Common: 2', 'Uncommon: 1', 'Rare: 2', 'Fixed: Bag of Industrial Plastic'];
  masterList['alch']['unholy affinity'] = ['Common: 1', 'Uncommon: 3', 'Rare: 1', 'Fixed: Blood Ice'];
  masterList['alch']['water breathing'] = ['Common: 4', 'Uncommon: 1', 'Rare: 0', 'Fixed: Bunch of Lilies'];
  masterList['components']['bag of industrial plastic'] = ['Rare'];
  masterList['components']['batch of leather'] = ['Rare'];
  masterList['components']['batch of mushrooms'] = ['Uncommon'];
  masterList['components']['blood ice'] = ['Uncommon'];
  masterList['components']['bottle of holy water'] = ['Common'];
  masterList['components']['bottle of paradise water'] = ['Common'];
  masterList['components']['bunch of daisies'] = ['Uncommon'];
  masterList['components']['bunch of lilies'] = ['Rare'];
  masterList['components']['bunch of paradise lilies'] = ['Uncommon'];
  masterList['components']['chunk of brass'] = ['Uncommon'];
  masterList['components']['chunk of iron'] = ['Rare'];
  masterList['components']['chunk of ivory'] = ['Uncommon'];
  masterList['components']['chunk of onyx'] = ['Rare'];
  masterList['components']['chunk of steel'] = ['Common'];
  masterList['components']['chunk of stygian iron'] = ['Common'];
  masterList['components']['femur'] = ['Common'];
  masterList['components']['gold ingot'] = ['Uncommon'];
  masterList['components']['handful of grave dirt'] = ['Common'];
  masterList['components']['healing herb'] = ['Uncommon'];
  masterList['components']['humerus'] = ['Common'];
  masterList['components']['lead brick'] = ['Uncommon'];
  masterList['components']['patch of lichen'] = ['Uncommon'];
  masterList['components']['patch of moss'] = ['Uncommon'];
  masterList['components']['piece of stygian coal'] = ['Common'];
  masterList['components']['piece of wood'] = ['Common'];
  masterList['components']['rose'] = ['Common'];
  masterList['components']['silver ingot'] = ['Uncommon'];
  masterList['components']['skull'] = ['Common'];
  masterList['components']['small bottle of gunpowder'] = ['Rare'];
  masterList['components']['soul ice'] = ['Uncommon'];
  masterList['components']['spool of copper wire'] = ['Rare'];
  masterList['components']['sprig of nightshade'] = ['Rare'];
  masterList['components']['stygian bone leech'] = ['Common'];
  return masterList;
}
