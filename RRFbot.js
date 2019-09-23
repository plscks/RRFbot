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
// []  Implement search rates lookup
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
        { name: "Description", value: "Lists searchable items starting with [LETTER]\nReturns search rate and locations of [ITEM NAME]", inline: true}
      ]
    }
  	});
	} else if (args[0] == 'list') {
		if (args[1] === undefined) message.channel.send('Please enter a letter or letters.');
		itemList(args[1].toLowerCase(), message);
	} else {
		var sortedItems = getNames(jsonData);
		if (!sortedItems.includes(args[0])) {
		  message.channel.send(args[0] + ' not found in database, check for a spelling error?');
		  return;
		} else {
			var itemData = jsonData[args[0].toLowerCase()];
			var sorted = sortResults(itemData);
			var percentText = ''
			var locationText = ''
			for (var i = 0; i < sorted.length; ++i) {
			  var percent = sorted[i][1];
			  if (percent < 1) percent = percent.toFixed(3);
			  else percent = percent.toPrecision(4)
				percentText += percent + '%\n'
				locationText += sorted[i] + '\n'
			}
			message.channel.send({embed: {
      	color: 3447003,
      	title: "Search odds for " + args[0],
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

function itemList(letterToList) {
	messageText = '';
	var itemsStartingWith = itemsStartWith(sortedItems, letterToList);
	for (i = 0; i < itemsStartingWith.length; ++i) messageText += itemsStartingWith[i] + '\n';
	message.channel.send({embed: {
      color: 3447003,
      title: "Items starting with " + letterToList.toUpperCase(),
      fields: [
        { name: "ITEMS:", value: messageText, inline: true}
      ]
    }
  });
}

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
