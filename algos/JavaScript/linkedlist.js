class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
class SList {
    constructor() {
        this.head = null;
        this.length = 0;
    }

    addFront(value){
        const n = new Node(value);
            if (!this.head){
                this.head = n;
            } else {
                n.next = this.head;
                this.head = n;
            }
        this.length++
        return this;
    }

    contains(value){
        let curr = this.head;
        while (curr){
            if (value === curr.value){
                console.log(curr.value);
                return true;
            }
            curr = curr.next;
        }
        return false;
    }
}


let list = new SList()
list.addFront('B').addFront('C').addFront('A').addFront('D').addFront('E').contains('F');
console.log(list);
