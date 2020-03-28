// Split list into multiple arrays of no more than X characters

// Initial list
let list = ["pants", "totally", "random", "words", "in", "this", "pants", "list", "gotta", "be", "enough", "for testing", "let us see", "what happens", "when", "I", "add", "more", "items", "to", "the", "initial", "list"];
console.log('Processing initial list.');
console.log(`Initial list: ${list.join(', ')}`);
console.log(`Shortening to 15 characters max per list.`);
let shortList = listShorten(list, 15);
for (var m = 0; m < shortList.length; m++) {
  console.log(`Shortened list number ${m}: ${shortList[m]}`);
}

function listShorten(list, maxLength) {
  let listLength = list.length;
  let outList = [];
  let finalList = [];
  let tempList = [];
  for (var i = 0; i < list.length; i++) {
    tempList.push(list[i]);
    count = charCount(tempList);
    if (count >= maxLength) {
      tempList.pop();
      outList.push(tempList);
      tempList = [];
      tempList.push(list[i]);
    }
  }
  outList.push(tempList);
  for (var k = 0; k < outList.length; k++) {
    outList[k] = outList[k].join(', ');
  }
  return outList
}

function charCount(inList) {
  let inListString = inList.join(", ");
  let inListCharCount = inListString.length;
  return inListCharCount
}
