# Nathan Saric - 02/04/2021

# Question 1: Binary Search Tree

# Node class used in BinarySearchTree class containing a single initialization function
class Node: 

    # Initialization function for Node class
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

# BinarySearchTree class containing an initialization function and 9 functions 
# that fulfill the requirements set out in Question 1
class BinarySearchTree:

    # Initialization function for BinarySearchTree class
    def __init__(self):
        self.rootNode = None

    # insert function that accepts a value and inserts the node into the BinarySearchTree in the correct location
    def insert(self, value):
        if self.rootNode == None:
            # Insert value as the root node of the tree
            self.rootNode = Node(value)
        else: 
            # Call the helper function to correctly insert the node into the tree
            return self.insertNodeBST(self.rootNode, value)

    # Helper function for the insert function 
    def insertNodeBST(self, currentNode, value):
        if value < currentNode.value:
            if currentNode.leftNode == None:
                # Insert node as the left child of the current node
                currentNode.leftNode = Node(value)
            else: 
                # Recursively call the helper function with the current node's left child
                return self.insertNodeBST(currentNode.leftNode, value)
        elif value > currentNode.value:
            if currentNode.rightNode == None:
                # Insert node as the left child of the current node 
                currentNode.rightNode = Node(value)
            else: 
                # Recursively call the helper function with the current node's right child
                return self.insertNodeBST(currentNode.rightNode, value)
        else: # value == currentNode.value
            # Duplicate value
            return

    # getTotalHeight function that returns the total height of a BinarySearchTree
    def getTotalHeight(self):
        # The tree is empty
        if self.rootNode == None:
            totalHeight = 0
        else:
            # Call the helper function to retrieve the height of the tree 
            totalHeight = self.getTotalHeightBST(self.rootNode)

        return totalHeight
    
    # Helper function for the getTotalHeight function 
    def getTotalHeightBST(self, currentNode):   
        if currentNode == None:
            treeHeight = 0
        else: 
            # Recursively call the helper function with the current node's left and right children
            treeHeight = (self.getTotalHeightBST(currentNode.leftNode)
                        + self.getTotalHeightBST(currentNode.rightNode)
                        + self.getNodeHeight(currentNode))

        return treeHeight

    # getNodeHeight function that returns the height of a given node in a BinarySearchTree
    def getNodeHeight(self, currentNode):
        if currentNode == None:
            nodeHeight = -1
        else:
            # Recursively call the function with the current node's left and right children
            leftTreeHeight = self.getNodeHeight(currentNode.leftNode)
            rightTreeHeight = self.getNodeHeight(currentNode.rightNode)
            nodeHeight = max(leftTreeHeight, rightTreeHeight) + 1

        return nodeHeight

    # getWeightBalanceFactor function that returns the weight balance factor of a BinarySearchTree
    def getWeightBalanceFactor(self):
        if self.rootNode == None:
            weightBalanceFactor = 0
        else:
            # Call the helper function to retrieve the weight balance factor of the tree
            weightBalanceFactor = self.getWeightBalanceFactorBST(self.rootNode)

        return weightBalanceFactor

    # Helper function for the getWeightBalanceFactor function
    def getWeightBalanceFactorBST(self, currentNode):
        if currentNode == None:
            weightBalanceFactor = 0
        else:
            # Call getNumNodes function to retrieve the number of nodes in the current node's left and right subtree
            numLeftNodes = self.getNumNodes(currentNode.leftNode)
            numRightNodes = self.getNumNodes(currentNode.rightNode)
            weightBalanceFactor = abs(numLeftNodes - numRightNodes) 

            # Recursively call the function with the current node's left and right children
            leftWeightBalanceFactor = self.getWeightBalanceFactorBST(currentNode.leftNode)
            rightWeightBalanceFactor = self.getWeightBalanceFactorBST(currentNode.rightNode)
            weightBalanceFactor = max(weightBalanceFactor, leftWeightBalanceFactor, rightWeightBalanceFactor)
        
        return weightBalanceFactor

    # getNumNodes function that returns the total number of nodes in a given node's left and right subtree
    def getNumNodes(self, currentNode):
        if currentNode == None:
            numNodes = 0 
        else:
            # Recursively call the function with the current node's left and right children
            leftNodes = self.getNumNodes(currentNode.leftNode)
            rightNodes = self.getNumNodes(currentNode.rightNode)
            numNodes = (leftNodes + rightNodes + 1)

        return numNodes

    # inOrderTraversal function used to print out the tree for testing purposes
    def inorderTraversal(self, currentNode):
        nodes = []
        if currentNode:
            nodes = self.inorderTraversal(currentNode.leftNode)
            nodes.append(currentNode.value)
            nodes += self.inorderTraversal(currentNode.rightNode)

        return nodes

# Test code
if __name__ == '__main__': 

    # BinarySearchTree from Figure 1 & Figure 2
    testSet = [[23, 16, 28, 4, 25], [6, 4, 9, 5, 8, 7]]

    for numbers in testSet:
        print('-' * 50)
        BST = BinarySearchTree()

        for i in range(0, len(numbers)):
            BST.insert(numbers[i])
            root = BST.rootNode
            print(BST.inorderTraversal(root))

        print("\nIn-Order Traversal of Tree: " + str(BST.inorderTraversal(root)))
        print("Height of Tree: " + str(BST.getTotalHeight()))
        print("Weight Balance Factor of Tree: " + str(BST.getWeightBalanceFactor()))
        print('-' * 50)
