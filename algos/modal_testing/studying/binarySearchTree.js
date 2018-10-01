function Node(val) {
    this.value = val;
    this.left = null;
    this.right = null;
}

function BST() {
    this.root = null;
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

BST.prototype.height = function () {
    current = this.root;
    if (!current) {
        return 0;
    }

    var leftHeight = current.left;
    var rightHeight = current.right;

    leftCount = 1;
    rightCount = 1; 
    while (leftHeight.left){
        leftHeight = leftHeight.left
        leftCount++;
        console.log('counting');
    }
    while (rightHeight.right){
        rightHeight = rightHeight.right
        rightCount++;
    }

    if (leftHeight > rightHeight){
        return leftCount + 1;
    } else {
        return rightCount + 1;
    }
}

BST.prototype.isBST = function (current) {
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

x = new BST()
// console.log(x);

x.push(10);
x.push(2);
x.push(3);
x.push(4);
x.push(22);
x.push(212);
x.push(12);
x.push(7);
x.push(1);

// console.log(x);
console.log(x.height());

    