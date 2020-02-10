// Testing database interactions with SQlite
// written by plscks
////////////////
// INIT STUFF //
////////////////
// Written by plscks
//////////////
// REQUIRES //
//////////////
const fs = require('fs');
const shell = require('shelljs');
const sqlite3 = require('sqlite3').verbose();
///////////////////
// DATABASE INIT //
///////////////////
var dbFile = './Testbot';
var dbExists = fs.existsSync(dbFile);

if (!dbExists) {
  fs.openSync(dbFile, 'w');
}

var db = new sqlite3.Database(dbFile);

if (!dbExists) {
  db.run('CREATE TABLE `your_table` (' +
    '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,' +
    '`name` TEXT,' +
    '`email` TEXT,');
}

// You can insert some data here in order to test
var statement = db.prepare('INSERT INTO `your_table` (`name`, `email`) ' + 'VALUES (?, ?)');

statement.run('Your name', 'some_random@email.com');
statement.finalize();

db.close();
///////////////////////////////////
// COMMAND LINE ARGUMENT PARSING //
///////////////////////////////////
var myArgs = process.argv.slice(2);
if (myArgs[0] === undefined || myArgs[0] === null) {
  console.log('Usage: node databaseTest.js [FLAG]');
  console.log('FLAGS:');
  console.log('        --help    This message');
  console.log('        -a        Add faction info to database "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
  console.log('        -s        Search Faction by name "-s [Faction Name]');
  console.log('        -r        Randomly select faction from database, defaults to only factions in top 10 use "A" to include all factions "-r (["A" for all factions])"');
  console.log('        -rm       Remove faction from database "-rm [Faction Name]"');
  process.exit();
}
var flag = myArgs[0].toLowerCase();
if (flag === '-a') {
  var argLength = myArgs.length;
  if (argLength < 9) {
    console.log('Please fill out all fields of "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
    process.exit();
  }
  var notInt = 0;
  for (var i = 1; i < argLength -1; i++) {
    if (isNaN(parseInt(myArgs[i]))) {
      notInt += 1
    } else {
      var facIDindex = i;
      i = argLength - 1;
    }
  }
  var facName = myArgs.slice(1,facIDindex).join(' ');
  var newArgs = [myArgs[0], facName, myArgs[facIDindex], myArgs[facIDindex + 1], myArgs[facIDindex + 2], myArgs[facIDindex + 3], myArgs[facIDindex + 4], myArgs[facIDindex + 5], myArgs[facIDindex + 6]];
  if (newArgs.length === 9) {
    var addName = newArgs[1].toLowerCase();
    var addID = parseInt(newArgs[2].toLowerCase());
    var addAlignment = newArgs[3].toLowerCase();
    var addX_coord = parseInt(newArgs[4]);
    var addY_coord = parseInt(newArgs[5]);
    var addPlane = newArgs[6].toLowerCase();
    var addHostile = newArgs[7].toLowerCase();
    var addTop10 = newArgs[8].toLowerCase();
    if (addTop10 === 'y') {
      addTop10 = true;
    } else if (addTop10 === 'n') {
      addTop10 = false;
    } else {
      console.log('Please use "Y" or "N" for is faction in top 10 or not.');
      process.exit();
    }
    var addFac = [addName, addID, addAlignment, addX_coord, addY_coord, addPlane, addHostile, addTop10];
    addFaction(addFac);
  } else {
    console.log('Please fill out all fields of "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
    process.exit();
  }
} else if (flag === '-s') {
  myArgs.shift();
  var searchFaction = myArgs.join(' ').toLowerCase();
} else if (flag === '-r') {
  if (!myArgs[1]) {
    var randTopTen = true;
  }
} else if (flag === '-rm') {
  myArgs.shift();
  var rmFaction = myArgs.join(' ').toLowerCase();
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
///////////////////////////
// ADD INPUT TO DATABASE //
///////////////////////////
function addFaction(facArray) {
  for (var i = 0; i < facArray.length; i++) {
    console.log(facArray[i]);
  }
}
/////////////////////////
// CLOSES THE DATABASE //
/////////////////////////
db.close((err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Close the database connection.');
});