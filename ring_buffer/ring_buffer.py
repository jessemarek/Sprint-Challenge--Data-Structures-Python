class RingBuffer:
    def __init__(self, capacity):
        # buffer needs a storage type and a max size(capacity)
        self.capacity = capacity
        self.storage = []
        self.current = 0

    def append(self, item):
        # if the buffer is already full, overwrite the oldest value
        if len(self.storage) == self.capacity:
            # if current index is not at the end
            # overwrite the item at our current location
            if (self.current + 1) <= self.capacity:
                self.storage.pop(self.current)
                self.storage.insert(self.current, item)
                self.current += 1
            # otherwise we need to move back to the frontand
            # overwrite our item there
            else:
                self.current = 0
                self.storage.pop(self.current)
                self.storage.insert(self.current, item)
                self.current += 1

        # otherwise add the value to the buffer
        else:
            self.storage.append(item)
            if self.current + 1 == self.capacity:
                self.current = 0
            else:
                self.current += 1

    def get(self):
        return self.storage
