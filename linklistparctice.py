# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' ')
#             current_node = current_node.next
#         print()

#     def Delete_first(self):
#         if self.head is None:
#             print('Nothing to delete, list is empty.')
#             return
#         self.head = self.head.next

#     def Delete_last(self):
#         if self.head is None:
#             print('List is empty.')
#             return
#         if self.head.next is None:
#             self.head = None
#             return
#         second_last = self.head
#         while second_last.next.next:
#             second_last = second_last.next
#         second_last.next = None

#     def Delete_by_value(self, value):
#         if self.head is None:
#             print("List is empty.")
#             return
#         if self.head.data == value:
#             self.head = self.head.next
#             return
#         current_node = self.head
#         while current_node.next and current_node.next.data != value:
#             current_node = current_node.next
#         if current_node.next is None:
#             print(f"Value {value} not found.")
#             return
#         current_node.next = current_node.next.next

# if __name__ == '__main__':
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(4)
#     linked_list.append(454)

#     print("Original List:")
#     linked_list.print_list()

#     linked_list.Delete_first()
#     print("After deleting the first node:")
#     linked_list.print_list()

#     linked_list.Delete_last()
#     print("After deleting the last node:")
#     linked_list.print_list()

#     linked_list.Delete_by_value(3)
#     print("After deleting node with value 3:")
#     linked_list.print_list()


    # Traversal  of linked list




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def traverse(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' ')
#             current_node = current_node.next
#         print()

# if __name__ == '__main__':
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(4)
#     # linked_list.append(5)

#     print("Traversing the linked list:")
#     linked_list.traverse()


# Search in a linklist


# class Node:
#     def __init__(self, data):  # Initialize Node with data
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)  # Create a new node with the given data
#         if self.head is None:
#             self.head = new_node  # If list is empty, make the new node the head
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node  # Append the new node at the end

#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' ')
#             current_node = current_node.next
#         print()

#     def search(self, key):
#         current_node = self.head
#         index = 0
#         while current_node:
#             if current_node.data == key:
#                 return f"Element {key} found at index {index}"
#             current_node = current_node.next
#             index += 1
#         return f"Element {key} not found in the list."

# if __name__ == '__main__':
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(4)
#     linked_list.append(454)

#     print("Original List:")
#     linked_list.print_list()

#     # Search for elements in the list
#     print(linked_list.search(3))  # Should print "Element 3 found at index 2"
#     print(linked_list.search(6))  # Should print "Element 6 not found in the list."
