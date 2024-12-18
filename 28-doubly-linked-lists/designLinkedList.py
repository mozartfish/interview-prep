# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
# Implement the MyLinkedList class:
#     MyLinkedList() Initializes the MyLinkedList object.
#     int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
#     void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#     void addAtTail(int val) Append a node of value val as the last element of the linked list.
#     void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
#     void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    def __init__(self, val):
        self.val = val 
        self.prev = None 
        self.next = None 

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right 
        self.right.prev = self.left 
        
    def get(self, index: int) -> int:
        curr = self.left.next 
        while curr and index > 0:
            curr = curr.next 
            index -= 1 
        if curr and curr != self.right and index == 0:
            return curr.val 
        return -1
        
    def addAtHead(self, val: int) -> None:
        node, nxt, prev = Node(val), self.left.next, self.left
        prev.next = node 
        nxt.prev = node 
        node.next = nxt 
        node.prev = prev 

    def addAtTail(self, val: int) -> None:
        node, nxt, prev = Node(val), self.right, self.right.prev 
        prev.next = node 
        nxt.prev = node 
        node.next = nxt 
        node.prev = prev
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next 
        while curr and curr and index > 0:
            curr = curr.next 
            index -= 1 
        if curr and index == 0:
            node, nxt, prev = Node(val), curr, curr.prev
            prev.next = node 
            nxt.prev = node 
            node.next = nxt 
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next 
        while curr and curr and index > 0:
            curr = curr.next 
            index -= 1 
        if curr and curr != self.right and index == 0:
            nxt, prev = curr.next, curr.prev
            nxt.prev = prev 
            prev.next = nxt 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)