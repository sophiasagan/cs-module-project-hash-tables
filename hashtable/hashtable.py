class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __str__(self):
    #     return "'{}' : '{}'".format(self.key, self.value)


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # how many indexes
        self.capacity = capacity
        # currently utilized slots
        self.size = 0
        # data structure (array length of capacity populated with default values)
        self.buckets = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        fnv_prime = 1099511628211
        offset_basis =  14695981039346656037
        hash_value = offset_basis
        key_utf8 = key.encode()
        for byte in key_utf8:
            hash_value = hash_value ^ byte
            hash_value = hash_value * fnv_prime
        return hash_value

        # # Constants
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # # FNV-1 Hash Function
        # hash = offset_basis + seed
        # for char in string:
        #     hash = hash * FNV_prime
        #     hash = hash ^ ord(char)
        # return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash = 5381

        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFFF

        # hash = 5381
        # byte_array = string.encode('utf-8')

        # for byte in byte_array:
        #     # the modulus keeps it 32-bit, python ints don't overflow
        #     hash = ((hash * 33) ^ byte) % 0x100000000

        # return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.size += 1
        index = self.hash_index(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = HashTableEntry(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = HashTableEntry(key, value)      

        # # generate hash based on key
        # slot = self.hash_index(key)
        # # increase size += 1
        # self.size += 1
        # # input value into buckets
        # self.buckets[slot] = HashTableEntry(key, value)

        # key_hash = djb2(key)
        # bucket_index = key_hash % self.capacity

        # new_node - _Node(key, value)
        # existing_node = self.bucket_array[bucket_index]

        # if existing_node:
        #     last_node = None
        #     while existing_node:
        #         if existing_node.key == key:
        #             # found existing key, replace value
        #             existing_node.value = value
        #             return
        #         last_node = existing_node
        #         existing_node = existing_node.next_node
        #     # if we get this far, we didn't find an existing key
        #     # so just append tht new node to the end of the bucket
        #     last_node.nex_node = new_node
        # else:
        #     self.bucket_array[bucket_index] = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        node = self.buckets[index]
        while HashTableEntry is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            print("Key is not found!")
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result 

        # self.size -= 1

        # self.put(key, None)

        # key_hash = djb2(key)
        # bucket_index = key_hash % self.capacity

        # existing_node = self.bucket_array[bucket_index]
        # if existing_node:
        #     last_node = None
        #     while existing_node:
        #         if existing_node.key == key:
        #             if last_node:
        #                 last_node.next_node = existing_node.next_node
        #             else:
        #                 self.bucket_array[bucket_index] = existing_node.next_node
        #         last_node = existing_node
        #         existing_node = existing_node.next_node

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

        # slot = self.hash_index(key)
        # hash_entry = self.buckets[slot]

        # if hash_entry is not None:
        #     return hash_entry.value

        # return None

        # key_hash = djb2(key)
        # bucket_index = key_hash % self.capacity

        # existing_node = self.bucket_array[bucket_index]
        # if existing_node:
        #     while existing_node:
        #         if existing_node.pair.key == key:
        #             return existing_node.pair.value
        #         existing_node = existing_node.next_node

        # return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_ht = HashTable(new_capacity)
        for entry in self.buckets:
            if entry:
                new_ht.put(entry.key, entry.value)
                if entry.next:
                    current = entry
                    while current.next:
                        current = current.next
                        new_ht.put(current.key, current.value)
        self.buckets = new_ht.buckets
        self.capacity = new_ht.capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
