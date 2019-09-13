// RRFbot implementation in node.js using discord.js
// No idea how this will go?
// Written by plscks
// Is this a test,
// It has to be.
// ###########
// ## TO DO ##
// ###########
// [x] Add sm timer for each individual user
// []  Make each individual user sm timer cancelable
const Discord = require('discord.js');
const client = new Discord.Client();
const talkedRecently = new Set();
const prefix = '!';

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

client.on('message', message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;
	const args = message.content.slice(prefix.length).split(' ');
	const command = args.shift().toLowerCase();
	if (command === 'ping') {
		console.log('incomming ping!');
		message.channel.send('Pong.');
		console.log('Arguments: ' + args[0]);
		console.log('Time converter to miliseconds: ' + args[0] * 1000);
	} else if (command == 'sm') {
		if (args[0] >= 1 && args[0] <= 65) {
			smTimer(message, args[0]);
		} else if (args[0] == 0) {
			talkedRecently.delete(message.author.id);
			message.channel.send('Removed Sorcerer\'s Might timer');
		}	else {
			message.channel.send('You must enter a real positive number of minutes between 1 and 65.');
		}
	}
});

function smTimer(msg, time) {
	if (talkedRecently.has(msg.author.id)) {
  	msg.channel.send('@' + msg.member.user.tag + ' you already have a Sorcerer\'s Might timer running. Use "!sm 0" to cancel it.');
	} else {
		msg.channel.send('Started SM timer for ' + time + ' minutes.');
		talkedRecently.add(msg.author.id);
		setTimeout(() => {
			msg.channel.send('Sorecerer\' Might will wear off of @' + msg.member.user.tag + ' in about one minute!');
			talkedRecently.delete(msg.author.id);
		}, time * 60000 - 60000);
	}
}
