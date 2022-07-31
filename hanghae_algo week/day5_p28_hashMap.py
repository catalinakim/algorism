class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        return self.dic[key] if key in self.dic else -1

    def remove(self, key: int) -> None:
        if key in self.dic:
            del self.dic[key]
        else:
            return

myHashMap = MyHashMap()
print(myHashMap.put(1, 1))  # The map is now [[1,1]]
print(myHashMap.put(2, 2))  # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))     # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))     # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(myHashMap.put(2, 1))  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))     # return 1, The map is now [[1,1], [2,1]]
print(myHashMap.remove(2))  # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))     # return -1 (i.e., not found), The map is now [[1,1]]