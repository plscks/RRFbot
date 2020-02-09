// Testing database interactions with SQlite
// written by plscks
////////////////
// INIT STUFF //
////////////////
const shell = require('shelljs');
///////////////////////////////////
// COMMAND LINE ARGUMENT PARSING //
///////////////////////////////////
var myArgs = process.argv.slice(2);
var flag = myArgs[0].toLowerCase();
if (flag === '-a') {
  var argLength = myArgs.lenth;
  for (var i = 1; i < argLength -1; i++) {
    if (parseInt(myArgs[i]))
  }
  if ( === 9) {
    var addName = myArgs[1].toLowerCase();
    var addID = myArgs[2].toLowerCase();
    var addAlignment = myArgs[3].toLowerCase();
    var addX_coord = myArgs[4];
    var addY_coord = myArgs[5];
    var addPlane = myArgs[6].toLowerCase();
    var addHostile = myArgs[7].toLowerCase();
    var addTop10 = myArgs[8].toLowerCase();
    if (addTop10 === 'y') {
      addTop10 = true;
    } else (addTop10 === 'n') {
      addTop10 = false;
    } else {
      console.log('Please use "Y" or "N" for is faction in top 10 or not.');
      process.exit();
    }
  } else {
    console.log('Please fill out all fields of "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
  }
} else (flag === '-s') {
  myArgs.shift();
  var searchFaction = myArgs.join(' ').toLowerCase();
} else (flag === '-r') {
  if (!myArgs[1]) {
    var randTopTen = true;
  } else (myArgs[1].toLowerCase() === 'a')
} else {
  console.log('Usage: node databaseTest.js [FLAG]');
  console.log('FLAGS:');
  console.log('        --help    This message');
  console.log('        -a        Add faction info to database "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
  console.log('        -s        Search Faction by name "-s [Faction Name]');
  console.log('        -r        Randomly select faction from database, defaults to only factions in top 10 use "A" to include all factions "-r (["A" for all factions])"');
  console.log('        -rm       Remove faction from database "-rm [Faction Name]"');
  process.exit();
}
