const exist = function(board, word) {
    const findNextLetter = (path, currentLetter) => {
        const pathCheck = path.map(pos => pos.join(''));
        const [currRow, currCol] = path[0];
        const nextPos = [ 
            board[currRow - 1] && board[currRow - 1][currCol] === word[currentLetter] ? [currRow - 1,currCol] : false,
            board[currRow + 1] && board[currRow + 1][currCol] === word[currentLetter] ? [currRow + 1,currCol] : false,
            board[currRow][currCol - 1] === word[currentLetter] ? [currRow, currCol - 1] : false,
            board[currRow][currCol + 1] === word[currentLetter] ? [currRow, currCol + 1] : false
        ].filter(pos => pos && !pathCheck.includes(pos.join('')));

        return nextPos.length || word.length === 1
           ? currentLetter === word.length - 1 || word.length === 1 ? true : nextPos.map(pos => findNextLetter([pos, ...path], currentLetter + 1)).some(check => check) : false;
    }
    return board.flatMap((row,rIndex) => row.map((col,cIndex) => col === word[0] 
        ? findNextLetter([[rIndex,cIndex]], 1)
        : false)).some(result => result);
};


//console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
//console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
//console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
console.log(exist([['a']], "a"))
