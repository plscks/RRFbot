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
console.log('Ready!');
});

client.login(token);

client.on('guildMemberAdd', member => {
	var leader = message.guild.roles.find(role => role.name === "Leader");
  member.guild.channels.get('481613088794083357').send('Welcome to the RRF! A <@&' + leader + '> will be with you shortly to get you access.');
});

client.on('message', message => {
	if (!message.content.startsWith(prefix)) return;
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
		message.reply('Initiating self update.....');
		console.log("Shutting down RRFbot for self update.....");
		setTimeout(() => {
			updateBot();
		}, 5000);
	} else if (command== 'test') {
		var admin = message.guild.roles.find(role => role.name === "Admin?");
		message.channel.send('Perhaps this will ping <@&' + admin + '>? We can only hope.....');
		console.log('first arg: ' + args[0] + ' second arg: ' + args[1] + ' third arg: ' + args[2]);
		console.log(typeof(args[0]));
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
  	console.log('Failed to update and restart');
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
        { name: "Command", value: "!items list [LETTER]\n!items [ITEM NAME]", inline: true},
        { name: "Description", value: "Lists searchable items starting with [LETTER(S)]\nReturns search rate and locations of [ITEM NAME]", inline: true}
      ]
    }
  	});
	} else if (args[0] == 'list') {
		if (args[1] === undefined) {
			message.channel.send('Please enter a letter or letters.');
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
			console.log('itemIn: ' + itemIn);
		  message.channel.send(itemIn + ' not found in database, check for a spelling error?');
		  return;
		} else {
			var itemData = jsonData[itemIn.toLowerCase()];
			var sorted = sortResults(itemData);
			var percentText = ''
			var locationText = ''
			for (var i = 0; i < sorted.length; ++i) {
			  var percent = sorted[i][1];
			  if (percent < 1) percent = percent.toFixed(3);
			  else percent = percent.toPrecision(4)
				percentText += percent + '%\n'
				locationText += sorted[i][0] + '\n'
			}
			message.channel.send({embed: {
      	color: 3447003,
      	title: "Search odds for " + itemIn,
      	fields: [
        	{ name: "Search Odds", value: percentText, inline: true},
        	{ name: "Location", value: locationText, inline: true}
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
	var itemsStartingWith = itemsStartWith(sortedItems, letterToList);
	var messageText = new Array(6);
	for (var i = 0; i < messageText.length; ++i) {
		messageText[i] = '';
	}
	for (var i = 0; i < messageText.length; ++i) {
		do {
				messageText[i] += itemsStartingWith[i] + '\n';
		}
		while (messageText[i] <= 1000);
	}
	for (var i = 0; i < messageText.length; ++i) {
		message.channel.send(messageText[i]);
	}
}
	/*
	for (i = 0; i < itemsStartingWith.length; ++i) {

		// This loop needs to be a for i=1 i < 6 ++i that changes variable messageTexti
		// then does a do/while loop until messageText is 1000 chracters
		// then finish the loop and change the variable
		messageText1 += itemsStartingWith[i] + '\n';
		if (messageText1.length > 1000) {
			console.log('messageText1: ' + messageText1.length);
			messageText2 += itemsStartingWith[i] + '\n';
			if (messageText2.length > 1000) {
				console.log('messageText2: ' + messageText2.length);
				messageText3 += itemsStartingWith[i] + '\n';
				console.log('messageText3: ' + messageText3.length);
			}
		}
	}
	console.log(messageText1);
	message.channel.send({embed: {
      color: 3447003,
      title: "Items starting with " + letterToList.toUpperCase(),
      fields: [
        { name: "ITEMS:", value: messageText1, inline: true}
      ]
    }
  });
	console.log(messageText2);
	if (messageText2 != '' && messageText3 == '') {
		return
	} else if (messageText3 = '' && messageText2 != '') {
		message.channel.send({embed: {
	      color: 3447003,
	      title: "Items starting with " + letterToList.toUpperCase() + " (continued)",
	      fields: [
	        { name: "ITEMS:", value: messageText2, inline: true}
	      ]
	    }
	  });
	} else if (messageText3 != '') {
			message.channel.send({embed: {
		      color: 3447003,
		      title: "Items starting with " + letterToList.toUpperCase() + " (continued)",
		      fields: [
		        { name: "ITEMS:", value: messageText3, inline: true}
		      ]
		    }
		  });
	}
*/


function itemsStartWith(masterList, letter) {
  var letterList = [];
  for (i = 0; i < masterList.length; ++i) {
    if (masterList[i].startsWith(letter)) {
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
