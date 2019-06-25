class MyHashMap:
    """
    不使用任何内建的哈希表库设计一个哈希映射

    具体地说，你的设计应该包含以下的功能：

        put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
        get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
        remove(key)：如果映射中存在这个键，删除这个数值对。

    示例：

    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);        
    hashMap.get(1);            // 返回 1
    hashMap.get(3);            // 返回 -1 (未找到)
    hashMap.put(2, 1);         // 更新已有的值
    hashMap.get(2);            // 返回 1
    hashMap.remove(2);         // 删除键为2的数据
    hashMap.get(2);            // 返回 -1 (未找到)

    注意：

        所有的值都在 [1, 1000000]的范围内。
        操作的总数目在[1, 10000]范围内。
        不要使用内建的哈希库。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/design-hashmap
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [[] for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = key % len(self.data)
        for idx, (k, v) in enumerate(self.data[h]):
            if k == key:
                self.data[h][idx] = (key, value)
                return
        self.data[h].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = key % len(self.data)
        for k, v in self.data[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = key % len(self.data)
        for k, v in self.data[h]:
            if k == key:
                self.data[h].remove((k, v))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 15616)
    obj.put(1, 98489)
    obj.put(1, 98489)
    obj.put(2, 123)
    p = obj.get(1)
    p2 = obj.get(2)
    obj.remove(2)
    p3 = obj.get(2)
    print(p)
    print(p2)
    print(p3)
