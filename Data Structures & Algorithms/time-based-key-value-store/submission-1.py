class TimeMap:

    def __init__(self):
        self.store = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.append((key, value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        found = False
        for i in self.store:
            if i[0] == key and i[2] <= timestamp:
                found = True
                res = i[1]

        if found:
            return res
        else:
            return ""
