// RRFbot implementation in node.js using discord.js
// No idea how this will go?
// Written by plscks
// Is this a test,
// It has to be.
// ###########
// ## TO DO ##
// ###########
// [X] Add sm timer for each individual user
// [X] Make each individual user sm timer cancelable
// [x] Add search rates lookup
// []  Add global commands embed if line starts with ! and isn't recognized
// [x] Implement search rates lookup
// []  Change search rates results to one row
// []  Add Component help
// []  Add alchemy help
// []  Add crafting help
const Discord = require('discord.js');
const shell = require('shelljs');
const client = new Discord.Client();
const talkedRecently = new Set();
const prefix = '!';
let jsonData = require('./searchRates.json');
jsonData = convertKeysToLowerCase(jsonData);
var sortedItems = getNames(jsonData);
var userID = [];

var myArgs = process.argv.slice(2);
var flag = myArgs[0];
if (flag == '-t') {
	var token = myArgs[1];
}
else {
	console.log('Usage: node RRFbot.js [FLAG]');
	console.log('FLAGS:');
	console.log('        --help    This message');
	console.log('        -t        Use auth token "-t [TOKEN-NUMBER]"');
	process.exit();
}

client.once('ready', () => {
console.log(getDateTime() + '> Ready!');
});

client.login(token);

client.on('guildMemberAdd', member => {
	var leader = message.guild.roles.find(role => role.name === "Leader");
  member.guild.channels.get('481613088794083357').send('Welcome to the RRF! A <@&' + leader + '> will be with you shortly to get you access.');
});

client.on('message', message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;
	const args = message.content.slice(prefix.length).split(' ');
	const command = args.shift().toLowerCase();
	if (command === 'greet') {
		message.channel.send('Hello and welcome to the RRF!');
	} else if (command == 'sm') {
		if (args[0] >= 0 && args[0] <= 65) {
			smTimer(message, args[0]);
		} else {
			message.reply('you must enter a real positive number of minutes between 1 and 65.');
		}
	} else if (command == 'items') {
		itemRates(args, message);
	} else if (command == 'update') {
		if (message.author.id !== '407383313335189515') return;
		message.reply('TESTbot is initiating self update.....');
		console.log(getDateTime() + "> Shutting down RRFbot for self update.....");
		setTimeout(() => {
			updateBot();
		}, 5000);
	} else if (command== 'test') {
		var admin = message.guild.roles.find(role => role.name === "Admin?");
		message.channel.send('Perhaps this will ping <@&' + admin + '>? We can only hope.....');
		console.log(getDateTime() + '> first arg: ' + args[0] + ' second arg: ' + args[1] + ' third arg: ' + args[2]);
		console.log(getDateTime() + '> ' + typeof(args[0]));
	}
});

function smTimer(message, time) {
	var smUser = message.member.displayName;
	if (time == 0) {
		if (!talkedRecently.has(message.author.id)) {
	  	message.channel.send(smUser + ' you don\'t have a Sorcerer\'s Might timer running. Use "!sm #" to start one.');
		} else {
			message.channel.send(smUser + ' canceled Sorcerer\'s Might.');
	 		clearTimeout(userID[message.author.id]);
			talkedRecently.delete(message.author.id);
		}
	} else {
		if (talkedRecently.has(message.author.id)) {
	  	message.reply('you already have a Sorcerer\'s Might timer running. Use "!sm 0" to cancel it.');
		} else {
			message.channel.send(smUser + ' started a Sorcerer\'s Might timer for ' + time + ' minutes.');
			talkedRecently.add(message.author.id);
			userID[message.author.id] = setTimeout(() => {
				var medic = message.guild.roles.find(role => role.name === "Medic");
				message.channel.send('<@&' + medic + '> Sorcerer\'s Might will wear off of ' + smUser + ' in about one minute!');
				talkedRecently.delete(message.author.id);
			}, time * 60000 - 60000);
		}
	}
}

function updateBot() {
	if (shell.exec('./update.sh').code !== 0) {
  	console.log(getDateTime() + '> Failed to update and restart');
  	shell.exit(1)
		return;
	} else {
		process.exit();
	}
}

function itemRates(args, message) {
	if (args[0] === undefined) {
		message.channel.send({embed: {
      color: 3447003,
      title: "Item Search Rates Lookup Usage:",
      fields: [
        { name: "!items search [KEYWORD]", value: "Searches for items and returns all matches to the search for [KEYWORD]. Note that extremely long lists will be DMed to you instead of displayed in channel.", inline: true},
        { name: "!items [ITEM NAME]", value: "Returns search rate and locations of [ITEM NAME] (rates account for location rate and NO OTHER bunuses or penalties)", inline: true}
      ]
    }
  	});
	} else if (args[0] == 'list') {
		message.channel.send('!items list has depreciated, please use `!items search [KEYWORD]` to search for items in database.');
		return;
	} else if (args[0] == 'search') {
		if (args[1] === undefined) {
			message.channel.send('Please enter a keyword to search for.');
			return;
		}
		itemList(args[1].toLowerCase(), message);
	} else {
		itemIn = ''
		for (i = 0; i < args.length; ++i) {
			itemIn += args[i] + ' ';
		}
		itemIn = itemIn.substring(0, itemIn.length - 1);
		itemIn = itemIn.toLowerCase();
		if (!sortedItems.includes(itemIn)) {
			console.log(getDateTime() + '> Item not found: ' + itemIn);

		  message.channel.send(itemIn + ' not found in database, check for a spelling error?');
		  return;
		} else {
			var itemData = jsonData[itemIn.toLowerCase()];
			var sorted = sortResults(itemData);
			var percentText = '';
			var locationText = '';
			var oddsText = '';
			var shortSorted = sorted.splice(0, 20);
			for (var i = 0; i < shortSorted.length; ++i) {
			  var percent = shortSorted[i][1];
			  if (percent < 1) percent = percent.toFixed(3);
			  else percent = percent.toPrecision(4)
				percentText += percent
				locationText += shortSorted[i][0] + '\n';
				oddsText += percent + '\%\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0' + shortSorted[i][0] + '\n';
			}
			console.log(oddsText);
			console.log(getDateTime() + '> Search rates requested for: ' + itemIn);
			message.channel.send({embed: {
      	color: 3447003,
      	title: "Top search odds for " + itemIn,
      	fields: [
        	{ name: "Search odds              Location", value: oddsText, inline: true},
      	]
    	}
  		});
		}
	}
}

function getNames(items) {
  var itemNames = [];
  for (var itemName in items) {
    itemNames.push(itemName);
  }
  return itemNames.sort()
}

function itemList(letterToList, message) {
	console.log(getDateTime() + '> Search input: ' + letterToList);
	var itemsStartingWith = itemsStartWith(sortedItems, letterToList);
	if (itemsStartingWith === undefined || itemsStartingWith.length == 0) {
		message.channel.send(letterToList + ' not found in the item database.');
		return;
	}
	while (itemsStartingWith.length) {
		smallList = itemsStartingWith.splice(0, 40);
		messageText = '';
		for (var i = 0; i < smallList.length; ++i) {
			messageText += smallList[i] + '\n';
		}
		if (letterToList.length <= 2 || letterToList == 'white' || letterToList == 'black' || letterToList == 'pair') {
			message.author.send({embed: {
		      color: 3447003,
		      title: "Items starting with " + letterToList.toUpperCase(),
		      fields: [
		        { name: "ITEMS:", value: messageText, inline: true}
		      ]
		    }
		  });
		} else {
			message.channel.send({embed: {
		      color: 3447003,
		      title: "Items starting with " + letterToList.toUpperCase(),
		      fields: [
		        { name: "ITEMS:", value: messageText, inline: true}
		      ]
		    }
		  });
		}
	}
}

function itemsStartWith(masterList, letter) {
  var letterList = [];
  for (i = 0; i < masterList.length; ++i) {
    if (masterList[i].includes(letter)) {
      letterList.push(masterList[i]);
    }
  }
  return letterList
}

function convertKeysToLowerCase(obj) {
    var output = {};
    for (i in obj) {
        if (Object.prototype.toString.apply(obj[i]) === '[object Object]') {
           output[i.toLowerCase()] = convertKeysToLowerCase(obj[i]);
        }else if(Object.prototype.toString.apply(obj[i]) === '[object Array]'){
            output[i.toLowerCase()]=[];
             output[i.toLowerCase()].push(convertKeysToLowerCase(obj[i][0]));
        } else {
            output[i.toLowerCase()] = obj[i];
        }
    }
    return output;
}

function sortResults(input) {
  var sortable = [];
  for (var location in input) {
    sortable.push([location, input[location]]);
  }

  var sortedItems = sortable.sort(function(a, b) {
    return b[1] - a[1];
  });

  return sortedItems
}

function getDateTime() {
  var date = new Date();
  var hour = date.getHours();
  hour = (hour < 10 ? "0" : "") + hour;
  var min  = date.getMinutes();
  min = (min < 10 ? "0" : "") + min;
  var sec  = date.getSeconds();
  sec = (sec < 10 ? "0" : "") + sec;
  var year = date.getFullYear();
  var month = date.getMonth() + 1;
  month = (month < 10 ? "0" : "") + month;
  var day  = date.getDate();
  day = (day < 10 ? "0" : "") + day;
  return year + ":" + month + ":" + day + ":" + hour + ":" + min + ":" + sec;
}
