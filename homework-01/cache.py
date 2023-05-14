import collections


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.data = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> str:
        if key not in self.data:
            return ""
        self.data.move_to_end(key)
        return self.data[key]

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.data.move_to_end(key)
            self.data[key] = value
            return

        self.data[key] = value
        if len(self.data) == self.capacity:
            self.data.popitem(last=False)

    def rem(self, key: str) -> None:
        if key in self.data:
            self.data.pop(key)
