/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 */

const guessCreator = (pick) => (num) => {
    return num === pick
       ? 0
       : num > pick ? -1 : 1
};

guess = guessCreator(1)

/**
 * @param {number} n
 * @return {number}
 */

const takeGuess = (range) => {
    const attempt = range[1] - Math.ceil((range[1] - range[0])/2)
    const response = guess(attempt)
    return response === 0
       ? attempt
       : response === -1 ? takeGuess([range[0],attempt]) : takeGuess([attempt,range[1]])
}

//Runtime: 56 ms, faster than 99.67% of JavaScript online submissions for Guess Number Higher or Lower.
//Memory Usage: 38.9 MB, less than 15.42% of JavaScript online submissions for Guess Number Higher or Lower.
const guessNumber = (n) => {
    const takeGuess = (range) => {
        const attempt = range[1] - Math.ceil((range[1] - range[0])/2)
        const response = guess(attempt)
        return response === 0
           ? attempt
           : response === -1 ? takeGuess([range[0],attempt]) : takeGuess([attempt,range[1]])
    }
   const first = guess(n)
   return first === 0 
    ? n
    : first === -1 ? takeGuess([1,n]) : takeGuess([n,(2 ** 31) - 1])
};

console.log(guessNumber(1))
