# Nathan Saric - 01/29/2021

# Question 4: Implementing Stack Using a Linked List

# Class used to create and initialize nodes used in the linked list
class Node: 

    def __init__(self, data):
        self.data = data
        self.next = None

# Class used to implement Stack using a linked list
class Stack:

    # This function initializes the head of the linked list to None
    def __init__(self):
        self.head = None

    # This function checks whether the current Stack instance is empty.
    # Returns True if the Stack is empty or returns False otherwise. 
    def isEmpty(self):
        if self.head == None:
            return True # Stack is empty
        else:
            return False # Stack is not empty

    # This function takes a data item as input and adds it onto the Stack.
    # No return value.
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # This function removes and returns the data item on the top of the Stack.
    def pop(self):
        if self.isEmpty():
            return None # returns None if Stack is empty
        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.data

    # This function retrieves and returns the data item on the top of the Stack. 
    def top(self):
        if self.isEmpty():
            return None # returns None if Stack is empty
        else:
            return self.head.data

    # This function retrieves and returns the number of data items in the Stack.
    def size(self):
        counter = self.head
        count = 0

        while counter:
            count += 1
            counter = counter.next
        return count

if __name__ == "__main__":
    newStack = Stack() # creates a new Stack instance
    print("Stack empty?: " + str(newStack.isEmpty())) # should print 'Stack empty?: True'

    newStack.push(10) # adds the value 10 into the Stack
    newStack.push(20) # adds the value 20 into the Stack
    newStack.push(30) # adds the value 30 into the Stack

    print("Stack size is " + str(newStack.size())) # should print 'Stack size is 3'
    print("Top element is " + str(newStack.top())) # should print 'Element on top is 30' 

    print("Removed " + str(newStack.pop()) + " from the Stack") # should print 'Removed 30 from the Stack"
    print("Removed " + str(newStack.pop()) + " from the Stack") # should print 'Removed 20 from the Stack"

    print("Stack size is " + str(newStack.size())) # should print 'Stack size is 1'
    print("Top element is " + str(newStack.top())) # should print 'Element on top is 10' 
    print("Stack empty?: " + str(newStack.isEmpty())) # should print 'Stack empty?: False'
