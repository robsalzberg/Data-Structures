class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # stores value at the end of the list
        # compares new value to previous
        # bubbles up if new value is greater than previous value
        self.storage.append(value)
        return self._bubble_up(self.get_size() - 1)

    def delete(self):
        # delete is to delete the max number in heap
        # swaps index 0 with the last index if the len of list is more than 1
        # then sift down to make sure the new max is at top
        # if only one value in heap then just delete the value
        # if nothing in heap then return false
      if len(self.storage) > 1:
          self.swap(0, len(self.storage)-1)
          max = self.storage.pop()
          self._sift_down(0)
      elif len(self.storage) == 1:
          max = self.storage.pop()
      else:
          max = False
      return max

    def get_max(self):
        return self.storage[0]

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
    # compares values in the heap
    # swaps if top value to left or right depending on the largest value
    # recursive to make sure all the values are in the right spot
        left = (index * 2) + 1
        right = (index * 2) + 2
        max = index
        if len(self.storage) > left and self.storage[max] < self.storage[left]:
            max = left
        if len(self.storage) > right and self.storage[max] < self.storage[right]:
            max = right
        if max != index:
            self.swap(index, max)
            self._sift_down(max)
  
  #helper function to swap indices
    def swap (self,a,b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]
