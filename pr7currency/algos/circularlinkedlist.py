class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.head.next = self.head  # Initialize the head's next to point to itself (circular)

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != self.head:  # Stop at the node before the head to append
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head  # Make it circular

    def length(self):
        cur = self.head
        total = 0
        while cur.next != self.head:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elements = []
        cur_node = self.head.next
        while cur_node != self.head:  # Iterate until we return to the head
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return " -> ".join(elements) if elements else "Empty List"

    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: out of range")
            return None
        cur_idx = 0
        cur_node = self.head.next
        while cur_idx <= index:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

    def erase(self, index):
        if index >= self.length() or index < 0:
            print("Error OUT OF RANGE")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_index <= index:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

    def __getitem__(self, index):
        return self.get(index)
    
    def insert(self, index, data):
        if index >= self.length() or index < 0:
            return self.append(data)
        cur_node = self.head
        cur_idx = 0
        while cur_idx <= index:
            prior_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = node(data)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            cur_idx += 1

    def inser_node(self, index, node):
        if index < 0:
            print("Error: Insert cannot be negative!")
            return
        if index >= self.length():
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = node
            node.next = self.head  # Maintain the circular link
            return
        cur_node = self.head
        cur_idx = 0
        while cur_idx <= index:
            prior_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                prior_node.next = node
                node.next = cur_node
                return
            cur_idx += 1
    
    def set(self, index, data):
        if index >= self.length() or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return
        cur_node = self.head.next
        cur_idx = 0
        while cur_idx <= index:
            if cur_idx == index:
                cur_node.data = data
                return
            cur_node = cur_node.next
            cur_idx += 1


# Example usage
nodes = int(input("How long is the list? "))
my_list = linked_list()

for index in range(nodes):
    data = input(f"What do you want to insert into the list at index {index + 1}? ")
    my_list.append(data)

print("Current Circular Linked List is: ", my_list.display())
