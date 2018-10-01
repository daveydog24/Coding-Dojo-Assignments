function Node(val) {
    this.value = val;
    this.left = null;
    this.right = null;
}

function BST() {
    this.root = null;
}

BST.prototype.isBST = function (node) {
    if (!node) {
        return true; 
    }
 
    if (node.left != null && node.left.value > node.value) { 
        return false;
    }
 
    if (node.right !=null && node.right.value < node.value) {
        return false;
    }
 
    if (!isBST(node.left) || !isBST(node.right)) {
        return false;
    }
 
    return true;  
}

BST.prototype.height = function (node) {
    if (!node) {
        return 0;
    }
    var leftHeight = height(node.left);
    var rightHeight = height(node.right);
 
    return Math.max(leftHeight, rightHeight) + 1;
}

BST.prototype.push = function(val) {
    var root = this.root;
 
    if (!root) {
       this.root = new Node(val);
       return;
    }
 
    var currentNode = root;
    var newNode = new Node(val); 
 
    while(currentNode) {
        if (val < currentNode.value) {
            if (!currentNode.left) {
                currentNode.left = newNode;
                break;
            } else {
                currentNode = currentNode.left;
            }
        } else {
            if (!currentNode.right) {
                currentNode.right = newNode;
                break;
            } else {
                currentNode = currentNode.right;
            }
        }
    }
}

x = new BST()
console.log(x);

x.push(10);
x.push(2);
x.push(3);
x.push(4);
x.push(22);
x.push(212);
x.push(12);
x.push(7);
x.push(1);

console.log(x);

    