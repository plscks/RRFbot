// Testing database interactions with SQlite
// written by plscks
////////////////
// INIT STUFF //
////////////////
// Written by plscks
//////////////
// REQUIRES //
//////////////
const shell = require('shelljs');
const sqlite3 = require('sqlite3').verbose();
////////////////////
// DATABASE STUFF //
////////////////////
let db = new sqlite3.Database('./Testbot', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the Testbot database.');
  arg_parse();
});
///////////////////////////////////
// COMMAND LINE ARGUMENT PARSING //
///////////////////////////////////
function arg_parse() {
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
    for (var i = 1; i < argLength - 1; i++) {
      if (isNaN(parseInt(myArgs[i]))) {
        notInt += 1
      } else {
        var facIDindex = i;
        i = argLength - 1;
      }
    }
    var facName = myArgs.slice(1, facIDindex).join(' ');
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
    var factionString = myArgs.join(' ').toLowerCase();
    searchFaction(factionString);
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
}
/////////////////////////////
// ADD FACTION TO DATABASE //
/////////////////////////////
function addFaction(facArray) {
  for (var i = 0; i < facArray.length; i++) {
    console.log(facArray[i]);
  }
  db.run(`INSERT INTO factions(faction_name, faction_id, alignment, x_coord, y_coord, plane, hostile, top_ten) VALUES("${facArray[0]}", "${facArray[1]}", "${facArray[2]}", "${facArray[3]}", "${facArray[4]}", "${facArray[5]}", "${facArray[6]}", "${facArray[7]}")`, function(err) {
    if (err) {
      return console.log(err.message);
    }
    // get the last insert id
    console.log(`${facArray[0]} ID: ${facArray[1]} has been added to the database.`);
  });
  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
}
//////////////////////////////////////
// SEARCH DATABASE FOR FACTION NAME //
//////////////////////////////////////
function searchFaction(searchString) {
  let db = new sqlite3.Database('./Testbot');

  let sql = `SELECT * FROM factions WHERE faction_name = ? ORDER BY faction_name`;

  db.each(sql, [`${searchString}`], (err, row) => {
    if (err) {
      throw err;
    }
    console.log(`top_ten: ${row.top_ten}`);
    if (row.top_ten) {
      var topMessage = 'This faction is in the top ten factions.';
    } else {
      var topMessage = 'This faction is not in the top ten factions';
    }
    console.log(`Faction: ${row.faction_name}    alignment: ${row.alignment}    location: (${row.x_coord}, ${row.y_coord} ${row.plane}) -- ${topMessage}`);
    console.log(`Link: https://www.nexusclash.com/modules.php?name=Game&op=faction&do=view&id=${row.faction_id}`);
  });
  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
}