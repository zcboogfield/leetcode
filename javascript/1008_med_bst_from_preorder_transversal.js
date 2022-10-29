// This was all quite fun, and good for you to do. But the assignment was literally just build the tree :upside_down:
const Node = (val, left, right) => ({
    val: (val===undefined ? 0 : val),
    left:  (left===undefined ? null : left),
    right: (right===undefined ? null : right),
});

const buildRootFromDepth = (nodes, currList) => {
    const nextNodes = nodes.flatMap(node => node && (node.left || node.right) ? [node.left, node.right] : undefined).filter(node => node !== undefined);
    return nextNodes.length
        ? buildRootFromDepth(nextNodes, [...currList, ...nodes.map(node => node ? node.val : node)])
        : [...currList, ...nodes.map(node => node ? node.val : node)];
}

//Runtime: 135 ms, faster than 10.66% of JavaScript online submissions for Construct Binary Search Tree from Preorder Traversal.
//Memory Usage: 40.7 MB, less than 10.15% of JavaScript online submissions for Construct Binary Search Tree from Preorder Traversal.
//Bascially you was fat and sassy on this one.
function TreeNode(val, left, right) {
     this.val = (val===undefined ? 0 : val)
     this.left = (left===undefined ? null : left)
     this.right = (right===undefined ? null : right)
}

const buildTree = (node, val) => { 
    return !node
    ? new TreeNode(val, undefined, undefined)
    : val > node.val 
        ? new TreeNode(node.val, node.left, buildTree(node.right, val))
        : new TreeNode(node.val, buildTree(node.left, val), node.right);
}


var bstFromPreorder = function(preorder) {
    return preorder.reduce((tree,val) => buildTree(tree, val), null)
};

//console.log();
//const response = bstFromPreorder([1,3]);
const response = bstFromPreorder([8,5,1,7,10,12]);
console.log(response);
//console.log(JSON.stringify(bstFromPreorder([1,3]), null, '\t'));
//[8,5,10,1,7,null,12]
