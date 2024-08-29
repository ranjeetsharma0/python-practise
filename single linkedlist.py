class Node:
    def __init__(self, data=None):
        self.data = data  # Set the node's data
        self.next = None  # Initialize next as None (no link yet)

# Example of creating nodes
node1 = Node(5)  # Node with data = 5
node2 = Node(10)  # Node with data = 10

# Linking nodes
node1.next = node2  # node1's next points to node2

# Now node1 is linked to node2
print(node1.data)  # Output: 5
print(node1.next.data)  # Output: 10
