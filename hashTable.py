class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size  # Initialize hash table with None values

    def _hash_function(self, key):
        return key % self.size  # Basic hash function using modulus

    def insert(self, key, value):
        index = self._hash_function(key)
        self.data[index] = value  # Store value at hashed index

    def search(self, key):
        index = self._hash_function(key)
        return self.data[index]  # Return value at hashed index

    def delete(self, key):
        index = self._hash_function(key)
        self.data[index] = None  # Delete value at hashed index

# Example usage:
if __name__ == "__main__":
    hash_table = HashTable(size=10)

    # Insert some key-value pairs
    hash_table.insert(10, "Value1")
    hash_table.insert(20, "Value2")
    hash_table.insert(30, "Value3")

    # Search for values by keys
    print("Value associated with key 20:", hash_table.search(20))  # Should print "Value2"
    print("Value associated with key 30:", hash_table.search(30))  # Should print "Value3"
    print("Value associated with key 40:", hash_table.search(40))  # Should print None (key not found)

    # Delete a key-value pair
    hash_table.delete(20)
    print("Value associated with key 20 after deletion:", hash_table.search(20))  # Should print None (key not found)