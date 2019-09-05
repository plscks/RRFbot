// RRFbot implementation in node.js using discord.js
// No idea how this will go?
// Written by plscks
// Is this a test,
// It has to be.
const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.login('your-token-goes-here');
