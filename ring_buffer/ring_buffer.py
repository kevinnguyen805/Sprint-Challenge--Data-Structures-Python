from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.cache = []

    def append(self, item):
        if self.storage.length >= self.capacity:
            value = self.cache[0]
            current_value = self.storage.head 
            while current_value.value is not value:
                current_value = current_value.next 
            current_value.value = item 
            self.cache = self.cache[1:]
            self.cache.append(item)
        else: 
            self.storage.add_to_tail(item)
            self.cache.append(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head

        # TODO: Your code here
        while current_node is not None: 
            current_value = current_node.value 
            list_buffer_contents.append(current_value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
