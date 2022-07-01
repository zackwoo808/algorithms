/**
 * Given an input string, output string, and a function, decide if the output string can be generated from the input string by applying the given function several times.
 * The given function's rules are as follows:
 * The function modifies the input string in place.
 * The function's parameters are as follows: def f(input_string, input_letter, output_letter) and it outputs the modified input string
 * The function takes one input letter and one output letter. For each instance of the input letter, the function replaces that input letter with the output letter:
   example f('input string', 'i', 'q') =>  'qnput strqng'
 */

const replaceFn = (input, inLetter, outLetter) => input.replace(new RegExp(inLetter, 'g'), outLetter);

const inputString = 'abcb';
const outputString = 'aded';

const solution = () => {
  if (inputString.length !== outputString.length) {
    return false;
  }

  if (inputString === outputString) {
    return true;
  }

  const hashTable = {};

  for (let i=0; i<inputString.length; i++) {
    const letter = inputString[i];
    if (!hashTable[letter]) {
      hashTable[letter] = outputString[i];
    } else if (hashTable[letter] !== outputString[i]) {
      return false;
    }
  }

  return true;
}

console.log(solution());