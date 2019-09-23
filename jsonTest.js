// Let's attempt to play around with json data imported in from .json file
// filename in question will be searchRates.json
// written by plscks
// Is this a test?
// It has to be.....
const fs = require('fs');
let jsonData = require('./searchRates.json');
jsonData = convertKeysToLowerCase(jsonData);


function getNames(items) {
  var itemNames = [];
  for (var itemName in items) {
    itemNames.push(itemName);
  }
  return itemNames.sort()
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
};

function itemsStartWith(masterList, letter) {
  var letterList = [];
  for (i = 0; i < masterList.length; ++i) {
    if (masterList[i].startsWith(letter)) {
      letterList.push(masterList[i]);
    }
  }
  return letterList
}

//////////

// INPUTS //
var item = 'chunk of ssteel';
var letterToList = 'c';
var sortedItems = getNames(jsonData);
var itemsStartingWith = itemsStartWith(sortedItems, letterToList);

// LIST ITEMS THAT CAN BE QUERIED
console.log('           ITEMS THAT CAN BE QUERIED');
console.log('+-----------------------------------------------+');
for (i = 0; i < itemsStartingWith.length; ++i) console.log('       ' + itemsStartingWith[i]);

// CHECK IF INPUT IN LIST
console.log(!sortedItems.includes(item));
if (!sortedItems.includes(item)) {
  console.log(item + ' not found in database check for a spelling error?');
  return;
}

//DISPLAY RESULTS
var itemData = jsonData[item.toLowerCase()];
var sorted = sortResults(itemData);
console.log('');
console.log('');
console.log('Information for ' + item);
console.log('Percent to Find        Location');
console.log('+----------------------------------------------+');
for (var i = 0; i < sorted.length; ++i) {
  var percent = sorted[i][1];
  if (percent < 1) percent = percent.toFixed(3);
  else percent = percent.toPrecision(4)
  console.log(percent + ' -------------- ' + sorted[i][0]);
}

//////////
/*
const query = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})


getNames(jsonData)
query.question(`What item are you searching for? : `, (item) => {
  var itemData = jsonData[item.toLowerCase()];
  var sorted = sortResults(itemData);
  for (var i = 0; i < sorted.length; ++i) {
    console.log(sorted[i][0] + ' has a ' + sorted[i][1].toFixed(2) + '% chance of finding a(n) ' + item);
  }
  query.close();
})
*/
