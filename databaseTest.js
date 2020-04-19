// Testing database interactions with SQlite
// written by plscks
//////////////
// REQUIRES //
//////////////
const sqlite3 = require('sqlite3').verbose();
////////////////////
// DATABASE STUFF //
////////////////////
const db = new sqlite3.Database('./Testbot', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the Testbot database.');
  arg_parse();
});
///////////////////////////////////
// COMMAND LINE ARGUMENT PARSING //
///////////////////////////////////
async function arg_parse() {
  var myArgs = process.argv.slice(2);
  for (var i = 0; i < myArgs.length; i++) {
    console.log(`Arg ${i} is ${myArgs[i]}`);
  }
  if (myArgs[0] === undefined || myArgs[0] === null) {
    console.log('Usage: node databaseTest.js [FLAG]');
    console.log('FLAGS:');
    console.log('        --help    This message');
    console.log('        -a        Add faction info to database "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
    console.log('        -s        Search Faction by name "-s [Faction Name]');
    console.log('        -r        Randomly select faction from database, defaults to only factions in top 10 use "A" to include all factions "-r (["A" for all factions])"');
    console.log('        -rm       Remove faction from database "-rm [Faction Name]"');
    console.log('        -raidAdd  Add scheduled raid to DB "-raidAdd [date] [time in UTC] [message] [leader] [faction]"');
    console.log('        -raidRM   Remove scheduled raid from DB "-rm [record number] [leader] [faction]"');
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
        addTop10 = 1;
      } else if (addTop10 === 'n') {
        addTop10 = 0;
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
    } else {
      var randTopTen = false;
    }
    randomFaction(randTopTen);
  } else if (flag === '-rm') {
    myArgs.shift();
    var rmFaction = myArgs.join(' ').toLowerCase();
    removeFaction(rmFaction);
  } else if (flag === '-raidadd') {
    const argLength = myArgs.length;
    if (argLength < 5 ) {
      console.log('        -raidAdd  Add scheduled raid to DB "-raidAdd [date] [time in UTC] [leader] [faction] [optional message]"');
      process.exit();
    } else if ( argLength === 5 ) {
      var message = null;
    } else {
      const messageArray = myArgs.slice(5, myArgs.length);
      var message = messageArray.join(' ');
    }
    const dateTest = myArgs[1];
    const timeTest = myArgs[2];
    const leader = myArgs[3]
    const faction = myArgs[4];
    if (!isValidDate(dateTest)) {
      console.log('Please use a date in "YYYY-MM-DD" format.');
      process.exit();
    } else if (!isValidTime(timeTest)) {
      console.log('Please usa a time in "HHMM" or "HH:MM" format.');
      process.exit();
    } else {
      const date = isValidDate(dateTest);
      const time = isValidTime(timeTest);
      addRaid(date, time, message, leader, faction);
    }
  } else if (flag === '-raidrm') {
    const argLength = myArgs.length;
    // should be 1 the extra 2 are for testing
    if (argLength !== 4) {
      console.log('        -raidRM   Remove scheduled raid from DB "-rm [record number] [leader] [faction]"');
      process.exit();
    } else {
      const record_no = myArgs[1];
      const leader = myArgs[2];
      const faction = myArgs[3];
      const canceledRaid = await getRecord('record_no', record_no);
      cancelRaid(record_no);
      console.log(`${leader} in ${faction} canceled raid record number ${record_no}: ${canceledRaid[0]['scheduled_date']} ${canceledRaid[0]['scheduled_time']} scheduled by ${canceledRaid[0]['raid_leader']} in ${canceledRaid[0]['raiding_faction']} on ${canceledRaid[0]['date_scheduled']}.`);
    }
  } else if (flag === '-raidcheck') {
    // Sara04/09/2020
    // @plscks perhaps a !scheduleraid function would be handy?
    // Have it send reminders 24 hours, 10 hours, 4 hours, 30 minutes in advance?
    const faction = `${myArgs[1]} ${myArgs[2]}`;
    console.log('Checking for upcomming raids...');
    const timeNow = Date.now();
    // raid time of 2020-04-17 02:00
    const dbPull = await getRecord('active', 1, faction);
    if (dbPull === 'No upcoming raid scheduled') {
      console.log(`${dbPull}`);
      process.exit();
    }
    console.log(JSON.stringify(dbPull, null, 4));
    dbPull.forEach((item) => {
      var raidDate = item['scheduled_date'];
      var raidTimeBase = item['scheduled_time'];
      var dateArray = raidDate.split('-');
      var timeArray = raidTimeBase.split(':');
      var raidTime = Date.UTC(dateArray[0], dateArray[1] - 1, dateArray[2], timeArray[0], timeArray[1]);
      var raidTimeArray = timeReturn(timeNow, raidTime);
      console.log(`scheduled raid: ${raidTimeArray[1]} days, ${raidTimeArray[2]} hours, ${raidTimeArray[3]} minutes. Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
    });
  } else if (flag === '-tickcheck') {
    // Sara04/09/2020
    // @plscks perhaps a !scheduleraid function would be handy?
    // Have it send reminders 24 hours, 10 hours, 4 hours, 30 minutes in advance?
    console.log('Checking for upcomming raids...');
    const timeNow = Date.now();
    const dbPull = await getRecord('active', 1, 'any');
    if (dbPull === 'No upcoming raid scheduled') {
      console.log(`${dbPull}`);
      process.exit();
    }
    dbPull.forEach((item) => {
      var raidDate = item['scheduled_date'];
      var raidTimeBase = item['scheduled_time'];
      var dateArray = raidDate.split('-');
      var timeArray = raidTimeBase.split(':');
      var raidTime = Date.UTC(dateArray[0], dateArray[1] - 1, dateArray[2], timeArray[0], timeArray[1]);
      if (raidTime < timeNow) {
        console.log('ALERT!');
        console.log(`canceling raid set for ${raidDate} ${raidTimeBase}, record number: ${item['record_no']}`);
        console.log('ALERT!');
        cancelRaid(item['record_no']);
      } else {
        // raidTimeArray[0] = total seconds
        // raidTimeArray[1] = days until
        // raidTimeArray[2] = hours until
        // raidTimeArray[3] = minutes until
        var raidTimeArray = timeReturn(timeNow, raidTime);
        var seconds = raidTimeArray[0];
        // one day = 86400 seconds
        // 10 hours = 36000 seconds
        // 4 hours = 14400 seconds
        // 30 minutes = 1800 seconds
        // 15 minutes = 900 seconds
        if (seconds >= 86380 && seconds <= 86420) {
          console.log('ALERT!');
          console.log(`scheduled raid in ${item['raiding_faction']}: ${raidTimeArray[1]} days, ${raidTimeArray[2]} hours, ${raidTimeArray[3]} minutes. Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
          console.log('ALERT!');
        } else if (seconds >= 35980 && seconds <= 36020) {
          console.log('ALERT!');
          console.log(`scheduled raid in ${item['raiding_faction']}: ${raidTimeArray[2]} hours, ${raidTimeArray[3]} minutes. Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
          console.log('ALERT!');
        } else if (seconds >= 14380 && seconds <= 14420) {
          console.log('ALERT!');
          console.log(`scheduled raid in ${item['raiding_faction']}: ${raidTimeArray[2]} hours, ${raidTimeArray[3]} minutes. Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
          console.log('ALERT!');
        } else if (seconds >= 1780 && seconds <= 1820) {
          console.log('ALERT!');
          console.log(`scheduled raid in ${item['raiding_faction']}: ${raidTimeArray[3]} minutes. Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
          console.log('ALERT!');
        } else if (seconds >= 880 && seconds <= 920) {
          console.log('ALERT!');
          console.log(`scheduled raid in ${item['raiding_faction']}: NEXT TICK!! Set for ${raidDate} ${raidTimeBase} ${item['raid_leader']} is raid leader, ${item['raid_message']}`);
          console.log('ALERT!');
        }
      }
    });
  } else {
    console.log('Usage: node databaseTest.js [FLAG]');
    console.log('FLAGS:');
    console.log('        --help    This message');
    console.log('        -a        Add faction info to database "-a [Faction Name] [Faction ID] [Faction Alignment] [x-coord] [y-coord] [Plane] [Hostile/Neutral/Friendly] [In top 10: Y/N]"');
    console.log('        -s        Search Faction by name "-s [Faction Name]');
    console.log('        -r        Randomly select faction from database, defaults to only factions in top 10 use "A" to include all factions "-r (["A" for all factions])"');
    console.log('        -rm       Remove faction from database "-rm [Faction Name]"');
    console.log('        -raidAdd  Add scheduled raid to DB "-raidAdd [date] [time in UTC] [leader] [faction] [optional message]"');
    console.log('        -raidRM   Remove scheduled raid from DB "-rm [record number] [leader] [faction]"');
    process.exit();
  }
}
////////////////////////////
// RETURN TIME UNTIL DATE //
////////////////////////////
function timeReturn(timeNow, raidTime) {
  const timeReturn = [];
  console.log(`current time: ${timeNow}   raid time: ${raidTime}`);
  // get total seconds between the times
  var delta = Math.abs(raidTime - timeNow) / 1000;
  timeReturn.push(delta);
  console.log(`total seconds between now and raid: ${delta}`);
  // calculate (and subtract) whole days
  var days = Math.floor(delta / 86400);
  timeReturn.push(days);
  delta -= days * 86400;
  console.log(`days: ${days}`);
  // calculate (and subtract) whole hours
  var hours = Math.floor(delta / 3600) % 24;
  timeReturn.push(hours);
  delta -= hours * 3600;
  console.log(`hours: ${hours}`);
  // calculate (and subtract) whole minutes
  var minutes = Math.floor(delta / 60) % 60;
  timeReturn.push(minutes);
  console.log(`minutes: ${minutes}`);
  return timeReturn
}
///////////////////
// SCHEDULE RAID //
///////////////////
function addRaid(date, time, message, leader, faction) {
  let sqlCHECK = `SELECT * from raid_schedule where scheduled_date = '${date}' AND scheduled_time = '${time}' AND raiding_faction = '${faction}'`;
  if (message === null) {
    let sqlINSERT = `INSERT INTO raid_schedule(raid_leader, raiding_faction, 	scheduled_date, scheduled_time) VALUES("${leader}", "${faction}", "${date}", "${time}")`
    db.get(sqlCHECK, async (err, rows) => {
      if (err) {
        return console.log(err.message);
      }
      if (rows === undefined) {
        db.run(sqlINSERT);
        const data = await getLastInsert();
        const record_no = data[0]['last_insert_rowid()'];
        console.log(`${leader} in ${faction} scheduled a raid for ${date} ${time} with the message ${message} and a record number of ${record_no}`);
      } else {
        console.log(`There is already a raid scheduled for ${date} at ${time}.`);
      }
    });
    db.close((err) => {
      if (err) {
        console.error(err.message);
      }
      console.log('Close the database connection.');
    });
  } else {
    let sqlINSERT = `INSERT INTO raid_schedule(raid_leader, raiding_faction, scheduled_date, scheduled_time, raid_message) VALUES("${leader}", "${faction}", "${date}", "${time}", "${message}")`
    db.get(sqlCHECK, async (err, rows) => {
      if (err) {
        return console.log(err.message);
      }
      if (rows === undefined) {
        db.run(sqlINSERT);
        const data = await getLastInsert();
        const record_no = data[0]['last_insert_rowid()'];
        console.log(`${leader} in ${faction} scheduled a raid for ${date} ${time} with the message ${message} and a record number of ${record_no}`);
      } else {
        console.log(`There is already a raid scheduled for ${date} at ${time}.`);
      }
    });
    db.close((err) => {
      if (err) {
        console.error(err.message);
      }
      console.log('Close the database connection.');
    });
  }
}
////////////////
// GET RECORD //
////////////////
function getRecord(column, value, faction) {
  var data = [];
  if (faction === 'any') {
    var sql = `SELECT * FROM "raid_schedule" WHERE ${column} = ${value} ORDER BY record_no DESC`;
  } else {
    var sql = `SELECT * FROM "raid_schedule" WHERE ${column} = ${value} AND raiding_faction = "${faction}" ORDER BY scheduled_date ASC, scheduled_time ASC LIMIT 2`;
  }
  return new Promise(resolve => {
        db.all(sql, (err,rows) => {
            if(err) {
                return console.error(err.message);
            }
            rows.forEach((row)=>{
                data.push(row);
            });
            resolve(data);
        });
    });
    if (data === undefined) {
      return 'No upcoming raid scheduled';
    } else {
      return data
    }
}
////////////////////////
// GET LAST INSERT ID //
////////////////////////
function getLastInsert() {
  var data = [];
  return new Promise(resolve => {
        db.all('SELECT last_insert_rowid() FROM "raid_schedule"', (err,rows) => {
            if(err) {
                return console.error(err.message);
            }
            rows.forEach((row)=>{
                data.push(row);
            });
            resolve(data);
        });
    });
    return data
}
///////////////////////////
// CANCEL SCHEDULED RAID //
///////////////////////////
function cancelRaid(record_no) {
  const sql = `UPDATE "raid_schedule" SET active = 0 WHERE record_no = ${record_no}`;
  db.run(sql);
  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
}
/////////////////////////////
// ADD FACTION TO DATABASE //
/////////////////////////////
function addFaction(facArray) {
  let sql = `INSERT INTO factions(faction_name, faction_id, alignment, x_coord, y_coord, plane, hostile, top_ten) VALUES("${facArray[0]}", "${facArray[1]}", "${facArray[2]}", "${facArray[3]}", "${facArray[4]}", "${facArray[5]}", "${facArray[6]}", "${facArray[7]}")`
  db.run(sql, function(err) {
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
  let sql = `SELECT * FROM factions WHERE faction_name = ? ORDER BY faction_name`;

  //db.each(sql, [`${searchString}`], (err, row) => {
  db.each(sql, [searchString], (err, row) => {
    if (err) {
      throw err;
    }
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
//////////////////////////
// GET A RANDOM FACTION //
//////////////////////////
function randomFaction(randTopTen) {
  if (randTopTen === true) {
    let sql = `SELECT * FROM factions WHERE top_ten = 1 ORDER BY RANDOM() LIMIT 1`;
    db.get(sql, (err, row) => {
      if (err) {
        return console.error(err.message);
      }
      if (row.top_ten) {
        var topMessage = 'This faction is in the top ten factions.';
      } else {
        var topMessage = 'This faction is not in the top ten factions';
      }
      console.log(`Faction: ${row.faction_name}    alignment: ${row.alignment}    location: (${row.x_coord}, ${row.y_coord} ${row.plane}) -- ${topMessage}`);
      console.log(`Link: https://www.nexusclash.com/modules.php?name=Game&op=faction&do=view&id=${row.faction_id}`);
    });
  } else {
    let sql = `SELECT * FROM factions ORDER BY RANDOM() LIMIT 1`;
    db.get(sql, (err, row) => {
      if (err) {
        return console.error(err.message);
      }
      if (row.top_ten) {
        var topMessage = 'This faction is in the top ten factions.';
      } else {
        var topMessage = 'This faction is not in the top ten factions';
      }
      console.log(`Faction: ${row.faction_name}    alignment: ${row.alignment}    location: (${row.x_coord}, ${row.y_coord} ${row.plane}) -- ${topMessage}`);
      console.log(`Link: https://www.nexusclash.com/modules.php?name=Game&op=faction&do=view&id=${row.faction_id}`);
    });
  }
  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
}
////////////////////////////////////////
// REMOVE A FACTION FROM THE DATABASE //
////////////////////////////////////////
function removeFaction(factionName) {
  let sql = `DELETE FROM factions WHERE faction_name =?`;
  db.run(sql, [factionName], function(err) {
    if (err) {
      return console.log(err.message);
    }
    // get the last insert id
    console.log(`${factionName} has been removed from the database.`);
  });
  db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
}
//////////////////////////////////////
// VARIFY DATE IS YYYY-MM-DD FORMAT //
//////////////////////////////////////
function isValidDate(dateString) {
  if(!/^\d{4}-\d{1}|\d{2}-\d{1}|\d{2}$/.test(dateString))
    return false

  const parts = dateString.split("-");
  const day = ('0' + parseInt(parts[2], 10)).slice(-2);
  const month = ('0' + parseInt(parts[1], 10)).slice(-2);
  const year = parseInt(parts[0], 10);

  if(year < 1000 || year > 3000 || month == 0 || month > 12)
    return false

  const monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

  if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0))
    monthLength[1] = 29;

  if (day > 0 && day <= monthLength[month - 1]) {
    const output = `${year}-${month}-${day}`;
    return output
  } else {
    return false
  }
}
/////////////////////////////////
// VERIFY TIME IS HH:MM FORMAT //
/////////////////////////////////
function isValidTime(timeString) {
  if(!/^\d{2}:\d{2}|\d{4}$/.test(timeString))
    return false;

  if (timeString.indexOf(':') > -1) {
    var parts = timeString.split(":");
    var hour = parts[0];
    var minute = parts[1];
  } else {
    var hour = timeString.slice(0,2);
    var minute = timeString.slice(2,4);
  }
  if (hour > 23 || minute > 59)
    return false;

  if (hour > -1 && minute > -1) {
    const output = `${hour}:${minute}`;
    return output
  } else {
    return false
  }
}
