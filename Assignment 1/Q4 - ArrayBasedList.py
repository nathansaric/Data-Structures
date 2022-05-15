# Nathan Saric - 01/29/2021

# Question 4: Implementing Stack Using an Array-Based List

# This function checks whether the current Stack instance is empty.
# Returns True if the Stack is empty or returns False otherwise. 
def isEmpty(stack):
    if len(stack) == 0:
        return True # Stack is empty
    else:
        return False # Stack is not empty

# This function takes a data item as input and adds it onto the Stack.
# No return value.
def push(stack, value):
    stack.append(value)

# This function removes and returns the data item on the top of the Stack.
def pop(stack):
    if len(stack) == 0:
        return None # returns None if Stack is empty
    else:
        return stack.pop()

# This function retrieves and returns the data item on the top of the Stack. 
def top(stack):
    if len(stack) == 0:
        return None # returns None if Stack is empty
    else:
        return(stack[-1])

# This function retrieves and returns the number of data items in the Stack.
def size(stack):
    return(len(stack))

if __name__ == "__main__":
    newStack = [] # creates a new Stack instance
    print("Stack empty?: " + str(isEmpty(newStack))) # should print 'Stack empty?: True'

    push(newStack, 10) # adds the value 10 into the Stack
    push(newStack, 20) # adds the value 20 into the Stack
    push(newStack, 30) # adds the value 30 into the Stack

    print("Stack size is " + str(size(newStack))) # should print 'Stack size is 3'
    print("Top element is " + str(top(newStack))) # should print 'Element on top is 30' 

    print("Removed " + str(pop(newStack)) + " from the Stack") # should print 'Removed 30 from the Stack"
    print("Removed " + str(pop(newStack)) + " from the Stack") # should print 'Removed 20 from the Stack"

    print("Stack size is " + str(size(newStack))) # should print 'Stack size is 1'
    print("Top element is " + str(top(newStack))) # should print 'Element on top is 10' 
    print("Stack empty?: " + str(isEmpty(newStack))) # should print 'Stack empty?: False'
