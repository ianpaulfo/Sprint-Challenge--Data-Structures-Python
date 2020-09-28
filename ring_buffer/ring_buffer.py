class RingBuffer:
    def __init__(self, capacity, data = []):
        self.index = 0
        self.capacity = capacity
        self.storage = list(data)[-capacity:]


    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item

        else:
            self.storage.append(item)
        self.index = (self.index + 1) % self.capacity

       
    def get(self):
        return [i for i in self.storage if i]

