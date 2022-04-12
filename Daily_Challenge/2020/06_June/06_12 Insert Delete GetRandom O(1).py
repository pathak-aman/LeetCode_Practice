from random import randint
class RandomizedSet:

    def __init__(self):
        self.dataStructure= dict()
        self.valuesInDataStructure = 0

    def insert(self, val: int) -> bool:
        if self.dataStructure.get(val):
            return False
        else:
            self.dataStructure[val] = True
            self.valuesInDataStructure+=1
            return True

    def remove(self, val: int) -> bool:
        if self.dataStructure.get(val):
            self.dataStructure.pop(val)
            self.valuesInDataStructure-=1
            return True
        else:
            return False

    def getRandom(self) -> int:
        self.randomPositionGenerated = randint(0,self.valuesInDataStructure-1)
        return list(self.dataStructure.keys())[self.randomPositionGenerated]

obj = RandomizedSet()

print(obj.insert(3))
print(obj.remove(5))
print(obj.insert(36))
print(obj.remove(3))
print(obj.insert(343))
print(obj.insert(2))

print(obj.getRandom())
print(obj.getRandom())
print(obj.insert(1))
print(obj.insert(67))
print(obj.insert(343))
print(obj.remove(5))
print(obj.getRandom())
print(obj.getRandom())
print(obj.insert(3))
print(obj.remove(5))
print(obj.valuesInDataStructure,obj.dataStructure)
print(obj.getRandom())