class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        return self._bubble_up(self.get_size() - 1)

    def delete(self):
        storage = self.storage

        storage[0], storage[self.get_size() - 1] = (
            storage[self.get_size() - 1],
            storage[0],)

        pop = storage.pop()
        self._sift_down(0)
        return pop

    def get_max(self):
        pass

    def get_size(self):
        return len(self.storage)

        # Note that index is the spot in the storage array that
        # the element we just appended to the storage array
        # currently occupies
    def _bubble_up(self, index):
        # 1. Check to see if the index is greater than zero
        # 2. Grab parent index
        # 3. Check if current value is greater than or less than parent value
        #     a. If current is greater than
        #     b. Swap
        # 4. If current is lesser than parent
        #     a. Leave it alone - break
        while index > 0:
            parent = (index - 1) // 2

            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent  # Updating your new index
            else:
                break

    def _sift_down(self, index):
        storage = self.storage
        max_child_index = None

        if index * 2 + 1 > self.get_size():
            return
        elif index * 2 + 2 >= self.get_size():
            max_child_index = index * 2 + 1
        elif storage[index * 2 + 1] > storage[index * 2 + 2]:
            max_child_index = index * 2 + 1
        else:
            max_child_index = index * 2 + 2

        if storage[index] < storage[max_child_index]:
            storage[index], storage[max_child_index] = (
                storage[max_child_index],
                storage[index],)
            self._sift_down(max_child_index)
        else:
            return
