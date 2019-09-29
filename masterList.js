let masterListData = require('./masterList.json');
console.log(masterListData['batch of leather']);
var masterListArray = [];
for (i in masterListData) {
  masterListArray.push([i, masterListData [i]]);
}
console.log('masterListArray:\n' + masterListArray);
for (var i = 0; i < masterListArray.length; ++i) {
  console.log('Item: ' + masterListArray[i][2]);
}
