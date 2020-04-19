function isValidDate(dateString) {
  if(!/^\d{4}-\d{1}|\d{2}-\d{1}|\d{2}$/.test(dateString))
    return false

  const parts = dateString.split("-");
  const day = ('0' + parseInt(parts[2], 10)).slice(-2);
  const month = ('0' + parseInt(parts[1], 10)).slice(-2); // , 10);
  const year = parseInt(parts[0], 10);
  console.log(`month: ${month}`);

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

const bad2Digit = '2020-37-14';
const bad1Digit = '2020-1-43';
const good1Digit = '2020-4-15';
const goodDate = '2020-04-15';
const badDate = '03/15/2020';

console.log(`good1Digit: ${good1Digit} valid? ${isValidDate(good1Digit)}`);
console.log(`goodDate: ${goodDate} valid? ${isValidDate(goodDate)}`);
console.log(`badDate: ${badDate} valid? ${isValidDate(badDate)}`);
console.log(`good1Digit: ${bad2Digit} valid? ${isValidDate(bad2Digit)}`);
console.log(`good1Digit: ${bad1Digit} valid? ${isValidDate(bad1Digit)}`);
