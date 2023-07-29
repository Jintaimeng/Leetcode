import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.index = {}
        self.length = 0
        self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.index.keys():
            self.dict[self.count] = val
            self.index[val] = self.count
            self.length += 1
            self.count += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index.keys():
            self.dict.pop(self.index[val])
            self.index.pop(val)
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        i = random.randint(0, self.length - 1)
        return self.dict[list(self.dict.keys())[i]]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()