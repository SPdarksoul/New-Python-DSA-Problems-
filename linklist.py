# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize next as None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the linked list is empty, set the new node as the head
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Iterate to the last node
        last_node.next = new_node  # Set the next of the last node to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()  # This print statement is outside the while loop

# Example usage:
if __name__ == '__main__':
    # Create a linked list
    linked_list = LinkedList()
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize next as None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the linked list is empty, set the new node as the head
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Iterate to the last node
        last_node.next = new_node  # Set the next of the last node to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()  # This print statement is outside the while loop


# Example usage:
if __name__ == '__main__':
    # Create a linked list
    linked_list = LinkedList()
    
    # Append some elements
    linked_list.append(4)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
   
    
    
    
    # Print the linked list
    linked_list.print_list()