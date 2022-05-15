# Nathan Saric - 02/04/2021

# Question 2.1: AVLTreeMap

# Node class used in AVLTreeMap class containing a single initialization function
class Node: 

    # Initialization function for Node class
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.leftNode = None
        self.rightNode = None

# AVLTreeMap class containing an initialization function and 9 functions 
# that fulfill the requirements set out in Question 2.1
class AVLTreeMap:

    # Initialization function for AVLTreeMap class
    def __init__(self):
        self.rootNode = None
    
    # get function that accepts a key and returns the value if the key exists in the AVLTree and returns None otherwise
    def get(self, key):
        # Call the helper function to retrieve the value if it exists
        return self.getKeyAVL(self.rootNode, key)

    # Helper function for the get function 
    def getKeyAVL(self, currentNode, key):
        if currentNode == None:
            # Key does not exist in the AVLtree
            return None
        
        if key < currentNode.key:
            # Recursively call the helper function with the current node's left child
            return self.getKeyAVL(currentNode.leftNode, key)
        elif key > currentNode.key:
            # Recursively call the helper function with the current node's right child
            return self.getKeyAVL(currentNode.rightNode, key)
        else: # key == currentNode.key
            # Key exists in the AVLTree
            return currentNode.value
    
    # put function that accepts a key and a value and inserts the pair into the AVLTree in the correct location
    def put(self, key, value):
        if self.rootNode == None:
            # Insert value as the root node of the tree
            self.rootNode = Node(key, value)
        else: 
            # Call the helper function to correctly insert the node into the tree
            self.rootNode = self.putKeyAVL(self.rootNode, key, value)

    # Helper function for the put function
    def putKeyAVL(self, currentNode, key, value):
        if currentNode == None:
            # Insert the node as a leaf node
            return Node(key, value)

        if key == currentNode.key:
            currentNode.value = value
            # Update the value if the key is already in the AVLtree
            return currentNode

        elif key < currentNode.key:
            # Recursively call the helper function with the current node's left child
            currentNode.leftNode = self.putKeyAVL(currentNode.leftNode, key, value)

        else: 
            # Recursively call the helper function with the current node's right child
            currentNode.rightNode = self.putKeyAVL(currentNode.rightNode, key, value)

        # Set the current node's height and calculate the balance factor to determine if the AVLTree needs to be rebalanced
        currentNode.height = max(self.getNodeHeight(currentNode.leftNode), self.getNodeHeight(currentNode.rightNode)) + 1
        balanceFactor = self.getBalanceFactor(currentNode)

        # Case 1: Left-Left Imbalance -> Right Rotate
        if balanceFactor > 1 and key < currentNode.leftNode.key:
                return self.rightRotation(currentNode)
        
        # Case 2: Left-Right Imbalance -> Left Rotate then Right Rotate
        elif balanceFactor > 1 and key > currentNode.leftNode.key: 
                currentNode.leftNode = self.leftRotation(currentNode.leftNode)
                return self.rightRotation(currentNode)
           
        # Case 3: Right-Right Imbalance -> Left Rotate
        elif balanceFactor < -1 and key > currentNode.rightNode.key:
                return self.leftRotation(currentNode)
           
        # Case 4: Right-Left Imbalance -> Right Rotate then Left Rotate
        elif balanceFactor < -1 and key < currentNode.rightNode.key:
                currentNode.rightNode = self.rightRotation(currentNode.rightNode)
                return self.leftRotation(currentNode)
        
        else:
            return currentNode

    # getNodeHeight function that returns the height of a given node in an AVLTree
    def getNodeHeight(self, currentNode):
        if currentNode == None:
            nodeHeight = 0
        else: 
            nodeHeight = currentNode.height

        return nodeHeight

    # getBalanceFactor function that returns the balance factor of a given node in an AVLTree
    def getBalanceFactor(self, currentNode):
        if currentNode == None:
            balanceFactor = 0
        else:
            # Call getNodeHeight function to retrieve the height of the current node's left and right subtree
            balanceFactor = self.getNodeHeight(currentNode.leftNode) - self.getNodeHeight(currentNode.rightNode)
        
        return balanceFactor

    # leftRotation function that performs a left rotation used in reblancing an AVLTree
    def leftRotation(self, currentNode):
        rotateNode = currentNode.rightNode
        tempNode = rotateNode.leftNode

        rotateNode.leftNode = currentNode
        currentNode.rightNode = tempNode

        # Update the current node and the rotated node's height 
        currentNode.height = max(self.getNodeHeight(currentNode.leftNode), self.getNodeHeight(currentNode.rightNode)) + 1
        rotateNode.height = max(self.getNodeHeight(rotateNode.leftNode), self.getNodeHeight(rotateNode.rightNode)) + 1
        
        return rotateNode

    # rightRotation function that performs a right rotation used in reblancing an AVLTree
    def rightRotation(self, currentNode):
        rotateNode = currentNode.leftNode
        tempNode = rotateNode.rightNode

        rotateNode.rightNode = currentNode
        currentNode.leftNode = tempNode

        # Update the current node and the rotated node's height 
        currentNode.height = max(self.getNodeHeight(currentNode.leftNode), self.getNodeHeight(currentNode.rightNode)) + 1
        rotateNode.height = max(self.getNodeHeight(rotateNode.leftNode), self.getNodeHeight(rotateNode.rightNode)) + 1

        return rotateNode

    # inOrderTraversal function used to print out the tree for testing purposes
    def inorderTraversal(self, currentNode):
        nodes = []
        if currentNode:
            nodes = self.inorderTraversal(currentNode.leftNode)
            nodes.append(currentNode.key)
            nodes += self.inorderTraversal(currentNode.rightNode)
        
        return nodes
        
# Test code
if __name__ == '__main__': 

    # Key-Value pairs provided in Question 2.1 Part 4)
    testSet = [[15, 'bob'], [20, 'anna'], [24, 'tom'],
            [10, 'david'], [13, 'david'], [7, 'ben'],
            [30, 'karen'], [36, 'erin'], [25, 'david']]

    AVL = AVLTreeMap()
    for pair in testSet:
        root = AVL.rootNode
        AVL.put(pair[0], pair[1])

    print('-' * 65)
    print("In-Order Traversal of Tree: " + str(AVL.inorderTraversal(root)))
    print("Test Valid Key: " + str(AVL.get(13)))
    print("Test Invalid Key: " + str(AVL.get(5)))

    # Updating value for existing key
    AVL.put(25, 'nathan')
    print("Test Updated Key: " + str(AVL.get(25)))
    print('-' * 65)
