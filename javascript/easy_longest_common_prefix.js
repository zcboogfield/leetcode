/**
 * @param {string[]} strs
 * @return {string}
 */
//Runtime: 88 ms, faster than 43.77% of JavaScript online submissions for Longest Common Prefix.
//Memory Usage: 39.8 MB, less than 64.57% of JavaScript online submissions for Longest Common Prefix.

const longestCommonPrefix = (strs) => {
   return strs.reduce((a,b) => a.length < b.length ? a : b)
        .split('')
        .reduce((acc,val,ind) => !acc.last && strs.every(str => str[ind] === val) 
            ? {...acc, prefix: acc.prefix + val }
            : {...acc, last: true}, 
            { prefix: '', last: false }).prefix
};

console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["dog","racecar","car"]));
