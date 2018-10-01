function Node(val) {
    this.value = val;
    this.left = null;
    this.right = null;
}

function BinarySearchTree() {
    this.root = null;
}

BinarySearchTree.prototype.isBST = function (node) {
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

BinarySearchTree.prototype.height = function (node) {
    if (!node) {
        return 0;
    }
    var leftHeight = height(node.left);
    var rightHeight = height(node.right);
 
    return Math.max(leftHeight, rightHeight) + 1;
}

BinarySearchTree.prototype.push = function(val) {
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
    