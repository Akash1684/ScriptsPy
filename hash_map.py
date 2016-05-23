table = [None]*10000

def store( string):
        """Input a string that's stored in
        the table."""
        hash_index = calculate_hash_value(string)
        if table[hash_index]:
            table[hash_index].append(string)
        else:
            table[hash_index]= [string]

def lookup(string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = calculate_hash_value(string)
        if table[index]:
            for each_key in table[index]:
                if each_key == string:
                    return string
        return -1

def calculate_hash_value(string):
        """Helper function to calulate a
        hash value from a string."""
        
        # hash_value is calculated as ** unicode(A)*100 + unicode(h) **
        
        return ord(string[0])*100+ord(string[1])


# Setup
print (calculate_hash_value('Akash'))

print (lookup('Akash'))

# Test store
store('Akash')
print (lookup('Akash'))
