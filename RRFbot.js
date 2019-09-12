// RRFbot implementation in node.js using discord.js
// No idea how this will go?
// Written by plscks
// Is this a test,
// It has to be.
const Discord = require('discord.js');
const client = new Discord.Client();

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
	if (message.content.toLowerCase() === '!ping') {
		message.channel.send('Pong.');
	}
});
