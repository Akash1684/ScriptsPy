class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_index = self.calculate_hash_value(string)
        if self.table[hash_index]:
            self.table[hash_index].append(string)
        else:
            self.table[hash_index]= [string]


    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = self.calculate_hash_value(string)
        if self.table[index]:
            for each_key in self.table[index]:
                if each_key == string:
                    return string
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0])*100+ord(string[1])


# Setup
hash_table = HashTable()

print (hash_table.calculate_hash_value('Akash'))

print (hash_table.lookup('Akash'))

# Test store
hash_table.store('Akash')
print (hash_table.lookup('Akash'))